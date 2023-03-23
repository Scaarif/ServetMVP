#!/usr/bin/env python3
from api.v1.views import db, populate_db, ServiceCategories, ServiceProviders, ServiceProviderServices, Locations, States, Countries, Reviews, Customers
from api.v1.views.application import app

stmt = db.select(ServiceProviders.first_name, ServiceProviders.last_name, ServiceProviderServices.image_uri, ServiceProviderServices.rating, ServiceProviderServices.service_description).select_from(ServiceProviderServices).join(Reviews, isouter=True).join(ServiceCategories).join(ServiceProviders).join(Locations).join(States).join(Countries).where(Locations.id==2)
