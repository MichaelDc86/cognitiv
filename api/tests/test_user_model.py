from api.models import User
from api import db
import unittest


class TestUserModel(unittest.TestCase):

    def test_encode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test',
            username='Test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test',
            username='Test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token) == 1)


if __name__ == '__main__':
    unittest.main()
