from flask import Flask
from scouting.db import get_firebase
from scouting.routes import register_routes


def create_app():
    app = Flask(__name__)

    with app.app_context():
        get_firebase()
    register_routes(app)

    return app
