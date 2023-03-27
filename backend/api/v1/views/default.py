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

    # see if it solves frontend issue
    # session['csrf_token'] = token

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
