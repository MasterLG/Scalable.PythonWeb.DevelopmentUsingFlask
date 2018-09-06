from application import create_app as creat_app_base
#from mongoengine.connection import _get_db, connect
import unittest

from user.models import User
print("0")


class UserTest(unittest.TestCase):
    def create_app(self):
        print("1")
        self.db_name = 'flaskbook_test'
        app.config.from_pyfile('settings-test.py')
        return create_app_base(
            #MONGODB_SETTINGS={'DB': self.db_name},
            # MONGO_DBNAME=app.config["MONGO_DBNAME"],
            # MONGODB_SETTINGS={'db': app.config["MONGO_DBNAME"], 'alias': 'default',
            #                   'username': app.config["MONGO_USERNAME"],
            #                   'password': app.config["MONGO_PASSWORD"],
            #                   'host': app.config["MONGO_URI"]},
            # alias="default",
            # db=app.config["MONGO_DBNAME"],
            # username=app.config["MONGO_USERNAME"],
            # password=app.config["MONGO_PASSWORD"],
            # host=app.config["MONGO_URI"],
            meta={'db_alias': 'aliasname'},
            TESTING=True,
            WTF_CSRF_ENABLED=False
        )

    def setUp(self):
        print("2")
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()

    def tearDown(self):
        print("3")
        #db = _get_db()
        # db.client.drop_database(db)
        # test_client
        pass

    def test_register_user(self):
        print("4")
        # basic registration
        rv = self.app.post('/register', data=dict(
            first_name="Jorge",
            last_name="Escobar",
            username="jorge",
            email="jorge@example.com",
            password="test123",
            confirm="test123"
        ), follow_redirects=True)
    assert User.objects.filter(username='jorge').count() == 1
