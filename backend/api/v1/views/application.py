#!/usr/bin/env python3
''' Application entry point.
'''
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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
