from unittest import TestCase

from api import app


def test_app_is_development(self):
    self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
    self.assertTrue(app.config['DEBUG'] is True)
    self.assertFalse(current_app is None)
    self.assertTrue(
        app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/flask_jwt_auth'
    )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/flask_jwt_auth_test'
        )
