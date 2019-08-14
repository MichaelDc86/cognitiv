import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'my.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://cognitiv:1234567@localhost:5432/my'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    # SECRET_KEY = b"(\xf2E\x1f\x9an'\xb32]j\x06\xb8\x01\xce\xe3\xef\r\xf4\xe0\x9dGT?"  # os.urandom(24)
