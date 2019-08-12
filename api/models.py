from api import db
# from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(128))
    # result = db.Column(JSON)

    def __repr__(self):
        return {self.username}
