from flask import Flask

# Factory


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    return app
