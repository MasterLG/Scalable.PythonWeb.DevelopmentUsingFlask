from flask import Flask
from flask_mongoengine import MongoEngine


db = MongoEngine()

# Factory


def create_app():
    
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    from user.views import user_app
    app.register_blueprint(user_app)
    db.connect(db=app.config["MONGO_DBNAME"], username=app.config["MONGO_USERNAME"],
               password=app.config["MONGO_PASSWORD"], host=app.config["MONGO_URI"])
    db.init_app(app)  # Initialize db
    return app



