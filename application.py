from flask import Flask
from flask_mongoengine import MongoEngine

print("5")
db = MongoEngine()
print("6")

# Factory


def create_app():
    print("7")
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    from user.views import user_app
    app.register_blueprint(user_app)
    db.connect(db=app.config["MONGO_DBNAME"], username=app.config["MONGO_USERNAME"],
               password=app.config["MONGO_PASSWORD"], host=app.config["MONGO_URI"])
    db.init_app(app)  # Initialize db
    return app


def get_test_db():
    db =
