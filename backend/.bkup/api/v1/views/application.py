#!/usr/bin/env python3
''' Application entry point.
'''
from flask_wtf.csrf import generate_csrf, CSRFProtect
# Protect against Cross Site Request Forgery
# csrf = CSRFProtect(app)

from api.v1.views import create_app
from flask_cors import CORS

app = create_app()

# Enable Cross Origin Resource Sharing
cors = CORS(
        app,
        resources={r"*": {"origins": "http://localhost:3000"}},
        expose_headers=["Content-Type", "X-CSRFToken"],
        supports_credentials=True,
        )

# Protect against Cross Site Request Forgery
# csrf = CSRFProtect(app)

'''
with app.test_request_context():
    print("###########---->", csrf_token())
    print("$$$$$$$$$$$---->", generate_csrf())
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0')
