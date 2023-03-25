#!/usr/bin/env python3
''' Default APIs.'''
from flask import (
        request, render_template, redirect,
        url_for, flash, abort, session, Blueprint,
        current_app, make_response, jsonify
        )
# from models import db, Customers, is_safe_url
from flask_login import (
        login_user, logout_user, login_required, current_user
        )
from api.v1.views import (
        db, ServiceProviders, ServiceCategories,
        ServiceProviderServices, Countries, States, Locations,
        Reviews, Customers
        )
from werkzeug.security import check_password_hash
from uuid import uuid4
from os import getenv
from flask_wtf.csrf import generate_csrf

# Blueprint for default apis
default_apis = Blueprint('default_apis', __name__, url_prefix='/api/v1')

testing = getenv('testing', '')


@default_apis.route("/getcsrf", methods=["GET"])
def get_csrf():
    token = generate_csrf()
    response = jsonify({"detail": "CSRF cookie set"})
    response.headers.set("X-CSRFToken", token)
    return response


@default_apis.route("/getsession", methods=["GET"])
def check_session():
    if current_user.is_authenticated:
        return jsonify({"login": True})

    return jsonify({"login": False})


if testing:
    @default_apis.route('/')
    def index():
        ''' Homepage for guests.
        '''
        # for testing
        from api.v1.views import Countries, States, Locations, ServiceCategories, db
        stmt = db.select(Locations)
        locations = db.session.scalars(stmt).all()
        stmt = db.select(Countries)
        countries = db.session.scalars(stmt).all()
        stmt = db.select(States)
        states = db.session.scalars(stmt).all()
        stmt = db.select(ServiceCategories)
        service_categories = db.session.scalars(stmt).all()
        return render_template('base.html', countries=countries, states=states, locations=locations, service_categories=service_categories, n=str(uuid4()))


@default_apis.route('/services')
def service_multi_post():
    ''' Returns summary data on seleted service-provider services.

        The selected services match the filters in the query string.
    '''
    from api.v1.views import (
            db, ServiceProviders, ServiceCategories,
            ServiceProviderServices, Countries, States, Locations,
            Reviews
            )
    # Retrieve query arguments
    country_id = request.args.get('country')  # required
    state_id = request.args.get('state')
    location_id = request.args.get('location')
    sc_id = request.args.get('service_category')  # required

    # Use filter parameters to fetch summary services data
    if not location_id:
        if not state_id:
            # use country id to filter
            stmt = db.select(ServiceProviders.first_name, ServiceProviders.last_name, ServiceProviders.id.label('sp_id'), ServiceProviderServices.image_uri, ServiceProviderServices.rating, ServiceProviderServices.service_description, ServiceProviderServices.id.label('sps_id')).select_from(ServiceProviderServices).join(ServiceCategories).join(ServiceProviders).join(Locations).join(States).join(Countries).where(Countries.id==int(country_id), ServiceCategories.id==int(sc_id))
            rows_list = db.session.execute(stmt).all()
            '''
            - returns a list of Row objects representing the result set
            - since columns were selected, each row (a Python named tuple) in
              the list will contain the column attributes requested
            - as in a named tuple, these attributes can be
              accessed using their column/attribute name e.g. row[0].name
            '''
        else:
            # use state id to filter
            stmt = db.select(ServiceProviders.first_name, ServiceProviders.last_name, ServiceProviders.id.label('sp_id'), ServiceProviderServices.image_uri, ServiceProviderServices.rating, ServiceProviderServices.service_description, ServiceProviderServices.id.label('sps_id')).select_from(ServiceProviderServices).join(ServiceCategories).join(ServiceProviders).join(Locations).join(States).where(States.id==int(state_id), ServiceCategories.id==int(sc_id))
            rows_list = db.session.execute(stmt).all()
    else:
        # use location id to filter
        stmt = db.select(ServiceProviders.first_name, ServiceProviders.last_name, ServiceProviders.id.label('sp_id'), ServiceProviderServices.image_uri, ServiceProviderServices.rating, ServiceProviderServices.service_description, ServiceProviderServices.id.label('sps_id')).select_from(ServiceProviderServices).join(ServiceCategories).join(ServiceProviders).join(Locations).where(Locations.id==int(location_id), ServiceCategories.id==int(sc_id))
        rows_list = db.session.execute(stmt).all()

    json_list = []

    for row in rows_list:
        # Prepare the data in json_serializable forms
        first_name = row.first_name
        last_name = row.last_name
        image_uri = row.image_uri
        rating = float(row.rating)  # for serializability
        description = row.service_description
        sps_id = row.sps_id
        sp_id = row.sp_id

        # A dictionary representing a single unit of data
        json_data = dict(first_name=first_name, last_name=last_name, image_uri=image_uri, rating=rating, description=description, sps_id=sps_id, sp_id=sp_id)

        # Append to list
        json_list.append(json_data)

    return jsonify(json_list)


@default_apis.route('/services/<sps_id>')
def service_one_get(sps_id):
    ''' Returns details about a specific service-provider service.
    '''
    # Fetch service details
    stmt = db.select(ServiceProviders.first_name, ServiceProviders.last_name, ServiceProviders.id, ServiceCategories.name, ServiceProviderServices.image_uri, ServiceProviderServices.rating, ServiceProviderServices.service_description).select_from(ServiceProviderServices).join(ServiceCategories).join(ServiceProviders).where(ServiceProviderServices.id==int(sps_id))
    details_row = db.session.execute(stmt).first()
    if not details_row:
        # No such service
        return make_response(jsonify({"status": "error", "message": "invalid sps ID"}), 400)

    # Fetch all reviews for the specified service
    stmt = db.select(Reviews.id, Reviews.review_content, Reviews.updated_at, Customers.first_name, Customers.last_name).join(Customers).join(ServiceProviderServices).where(ServiceProviderServices.id==int(sps_id))
    reviews_rows_list = db.session.execute(stmt).all()
    ''' returns list of reviews details rows.'''

    # Prepare the data in json_serializable forms
    first_name = details_row.first_name
    last_name = details_row.last_name
    image_uri = details_row.image_uri
    rating = float(details_row.rating)  # for serializability
    description = details_row.service_description
    sp_id = details_row.id

    json_data = dict(first_name=first_name, last_name=last_name, image_uri=image_uri, rating=rating, description=description, serviceProvider_id=sp_id)

    # Prepare list of reviews and associated details
    reviews = []
    for reviews_row in reviews_rows_list:
        content = reviews_row.review_content
        updated_at = reviews_row.updated_at.isoformat()  # make serializable
        first_name = reviews_row.first_name
        last_name = reviews_row.last_name
        review_id = reviews_row.id
        review_json = dict(review_id=review_id, content=content, customer_first_name=first_name, customer_last_name=last_name, updated_at=updated_at)
        reviews.append(review_json)

    # Add reviews list to return data
    json_data.update({"reviews": reviews})

    return jsonify(json_data)



















"""
@sp_auth_views.route('/login')
def sp_login():
    ''' Return the login form view.'''
    return render_template('sp_auth/login.html')


@sp_auth_views.route('/login', methods=['POST'])
def sp_login_post():
    ''' Authenticate posted login information, and log servuce provider in.
    '''
    from api.v1.views import db, ServiceProviders, is_safe_url
    # Retrieve provided login information
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    # Verify that service provider is registered
    stmt = db.select(ServiceProviders).where(ServiceProviders.username==username)
    row = db.session.execute(stmt).first()  # returns Row object or None
    if row:
        # Valid username
        sp = row[0]
    else:
        sp = None

    # Handle failed authentication
    if not sp or not check_password_hash(sp.password, password):
        # Flash an error message to display
        flash("Invalid username and/or password", "invalid_usr_pwd")
        # Redirect to login page to try again
        return redirect(url_for('sp_auth_views.sp_login'))

    # Service provider exists and is authenticated
    session['account_type'] = 'service_provider'
    login_user(sp, remember=remember)  # log in the user into session

    # flash('Logged in successfully.')

    # Retrieve next URL, if available
    nextp = request.args.get('next')
    '''
    When a logged-out user tries to access a protected page (login_required),
    they get redirected to login, and a `next` query string parameter is
    attached to the URL of the POST login link. The value of this parameter is
    the URL the user attempted to visit before redirection.
    '''

    # Protect against Open Redirect attacks
    if not is_safe_url(nextp):
        abort(400, description="`next` URL not safe")

    return redirect(nextp or url_for('sp_auth_views.sp_profile', id=sp.id))


@sp_auth_views.route('/<id>/profile')
@login_required
def sp_profile(id):
    ''' Service provider profile endpoint.
    '''
    return render_template('sp_auth/profile.html')


@sp_auth_views.route('/<id>/profile/edit')
@login_required
def sp_profile_get(id):
    ''' Returns service provider profile-editing form.
    '''
    # fetch all locations for testing; should later be removed
    from api.v1.views import Locations, db
    stmt = db.select(Locations)
    locations = db.session.scalars(stmt).all()
    return render_template('sp_auth/profile_edit.html', id=id, n=str(uuid4()), locations=locations)


@sp_auth_views.route('/<id>/profile/edit', methods=['POST'])
def sp_profile_put(id):
    ''' Processes form data to update a service provider's record.
    '''
    from api.v1.views import db, ServiceProviders
    # Collect update details
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')  # unique
    phone = request.form.get('phone')  # unique
    username = request.form.get('username') # must be unique in storage
    location_id = request.form.get('location')
    whatsapp = request.form.get('whatsapp')
    # todo: validate and save image to file system :done VSFS
    image = request.files.get(
            'profile_pic')  # file object representing image data

    # Retrieve service provider object from database
    stmt = db.select(ServiceProviders).where(ServiceProviders.id==id)
    existing_sp = db.session.scalars(stmt).first()

    # Validate username
    if username:
        stmt = db.select(ServiceProviders).where(ServiceProviders.username==username)
        sp = db.session.scalars(stmt).first()
        if not existing_sp.username==username and sp:
            # username already exists
            flash(
                    'username already exists. Please try another',
                    'username_exists'
                    )  # include message category
            return redirect(url_for('sp_auth_views.sp_profile_get', id=id, n=str(uuid4())))
        existing_sp.username = username

    if not username:
        old_username = existing_sp.username

    # Set image identifier
    if image.filename or username:
        # If the user does not select a file, the browser submits an...
        # ...empty file without a filename ('').
        if username:
            image_uri = current_app.config["SP_IMAGE_RPATH"] + username + '.jpg'
        else:
            # New profile pic but old username
            image_uri = current_app.config["SP_IMAGE_RPATH"] + old_username + '.jpg'
        # todo: implement deleting image files...
        # ...redundant as a result of a change of usernames
    else:
        image_uri = None

    # Validate email
    if email:
        stmt = db.select(ServiceProviders).where(ServiceProviders.email==email)
        sp = db.session.scalars(stmt).first()
        if not existing_sp.email==email and sp:
            # email already exists
            flash('email already exists. Please try another', 'email_exists')
            return redirect(url_for('sp_auth_views.sp_profile_get', id=id, n=str(uuid4())))
        existing_sp.email = email

    # Validate phone
    if phone:
        stmt = db.select(ServiceProviders).where(ServiceProviders.phone==phone)
        sp = db.session.scalars(stmt).first()
        if not existing_sp.phone==phone and sp:
            # phone number already exists
            flash('phone already exists. Please try another', 'phone_exists')
            return redirect(url_for('sp_auth_views.sp_profile_get', id=id, n=str(uuid4())))
        existing_sp.phone = phone

    # Update service provider record with validated data
    if first_name:
        existing_sp.first_name = first_name
    if last_name:
        existing_sp.last_name = last_name
    if image_uri:
        existing_sp.image_uri = image_uri
    if location_id:
        existing_sp.location_id = int(location_id)
    if whatsapp:
        existing_sp.whatsapp = whatsapp

    db.session.add(existing_sp)
    db.session.commit()

    # Save image to file system ONLY now
    if image.filename:
        image.save(
                current_app.config["SP_IMAGE_PATH"] + username + '.jpg'
                )  # VSFS

    return redirect(url_for('sp_auth_views.sp_profile', id=id))


@sp_auth_views.route('/')
def sp_index():
    ''' Endpoint for site homepage.
    '''
    return render_template('baseSP.html')


@sp_auth_views.route('/logout')
@login_required
def sp_logout():
    ''' Log a sign-in user out of the session.
    '''
    logout_user()
    return redirect(url_for('sp_auth_views.sp_index'))


@sp_auth_views.route('/signup')
def sp_signup():
    ''' Return signup form.'''
    # Retrieve all locations; for testing and should later be removed
    from api.v1.views import Locations, db
    stmt = db.select(Locations)
    locations = db.session.scalars(stmt).all()
    return render_template('sp_auth/signup.html', val=str(uuid4()), locations=locations)


@sp_auth_views.route('/signup', methods=['POST'])
def sp_signup_post():
    ''' Process service provider registration.
    '''
    from api.v1.views import db, ServiceProviders
    # Collect registration details
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')  # unique
    phone = request.form.get('phone')  # unique
    username = request.form.get('username') # must be unique in storage
    password = request.form.get('password')
    location_id = request.form.get('location')
    whatsapp = request.form.get('whatsapp')
    # todo: validate and save image to file system :done VSFS
    image = request.files.get(
            'profile_pic')  # file object representing image data

    # Validate username
    stmt = db.select(ServiceProviders).where(ServiceProviders.username==username)
    sp = db.session.scalars(stmt).first()
    if sp:
        # username already exists
        flash(
                'username already exists. Please try another',
                'username_exists'
                )  # include message category
        return redirect(url_for('sp_auth_views.sp_signup', id=str(uuid4())))
    # else set image identifier
    if image.filename:
        # If the user does not select a file, the browser submits an...
        # ...empty file without a filename ('').
        image_uri = current_app.config["SP_IMAGE_RPATH"] + username + '.jpg'
    else:
        image_uri = None

    # Validate email
    stmt = db.select(ServiceProviders).where(ServiceProviders.email==email)
    sp = db.session.scalars(stmt).first()
    if sp:
        # username already exists
        flash('email already exists. Please try another', 'email_exists')
        return redirect(url_for('sp_auth_views.sp_signup', id=str(uuid4())))

    # Validate phone
    stmt = db.select(ServiceProviders).where(ServiceProviders.phone==phone)
    sp = db.session.scalars(stmt).first()
    if sp:
        # phone number already exists
        flash('phone already exists. Please try another', 'phone_exists')
        return redirect(url_for('sp_auth_views.sp_signup', id=str(uuid4())))

    # Persist validated data to database
    new_sp = ServiceProviders(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            username=username,
            password=password,
            image_uri=image_uri,
            location_id=int(location_id),
            whatsapp=whatsapp
            )
    db.session.add(new_sp)
    db.session.commit()

    # Save image to file system ONLY now
    if image.filename:
        image.save(
                current_app.config["SP_IMAGE_PATH"] + username + '.jpg'
                )  # VSFS

    return redirect(url_for('sp_auth_views.sp_login'))


@sp_auth_views.route('<id>/static/<path:uri>')
def sp_static(id, uri):
    ''' Endpoint for static file requests.
    '''
    return redirect(url_for('static', filename=uri))
"""
