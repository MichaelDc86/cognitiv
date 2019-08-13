from flask import jsonify, request
import json
from flask_restful import Resource, Api, reqparse

from api import app

from api.models import User
from api import db, bcrypt

from api.decorators import is_admin_user, login_required

api = Api(app)


class UserCrud(Resource):

    @staticmethod
    def get_user():
        context = request.headers
        user = User.query.filter_by(id=int(context.get('logged_in_user'))).first()
        return user

    @staticmethod
    def get_context():
        context = request.form
        return context

    @staticmethod
    def get_request():
        return request

    @staticmethod
    def get(user_id=None):
        users_list = []
        if user_id and user_id != 'favicon.ico':
            users = User.query.filter_by(id=int(user_id[-1::])).first()
            return jsonify({'users': users.username})
        else:
            users = User.query.all()
            for user in users:
                users_list.append({user.id: user.username})
            return jsonify({'users': users_list})

    @login_required
    @is_admin_user
    def post(self, user_id=None):
        data = self.validate_data()
        if data:
            if data.get('is_admin') == 'True' or data.get('is_admin') == '1':
                data['is_admin'] = True
            cur_user = User.query.filter_by(username=data.get('username')).first()
            if not cur_user:
                new_user = User(
                    username=data.get('username'),
                    email=data.get('email'),
                    is_admin=data.get('is_admin'),
                    password=data.get('password'),
                )
                db.session.add(new_user)
                db.session.commit()

                auth_token = new_user.encode_auth_token(new_user.id)
                response = {
                    'status': 'success',
                    'message': 'Successfully created!',
                    'auth_token': auth_token.decode()
                }
                return json.dumps(response), 201
                # return jsonify(f'user {new_user} was created!')
            else:
                return jsonify(f'User {cur_user} already exists. Please Log in.')
        else:
            return jsonify(f'Incorrect request data')

    @login_required
    @is_admin_user
    def delete(self, delete_id):
        user = User.query.filter_by(id=int(delete_id[-1::])).first()
        db.session.delete(user)
        db.session.commit()

        return jsonify(f'User {user} was deleted!')

    @staticmethod
    def validate_data():

        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True,  location='form')
        parser.add_argument('email', type=str, location='form')
        parser.add_argument('is_admin', type=str, location='form')
        parser.add_argument('password', type=str, required=True, location='form')
        args = parser.parse_args()
        return args


class LoginAPI(Resource):

    def post(self):
        post_data = request.form

        try:

            user = User.query.filter_by(
                email=post_data.get('email')
              ).first()
            if user and bcrypt.check_password_hash(
                    user.password, post_data.get('password')
            ):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode(),
                        'user_id': str(user.id)
                    }

                    return json.dumps(response), 200
            else:
                response = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return json.dumps(response), 404

        except Exception as e:
            print(e)
            # response = {
            #     'status': 'fail',
            #     'message': 'Try again'
            # }
            return jsonify(status='fail', message='Try again'), 500


api.add_resource(UserCrud, '/', '/<string:user_id>', '/user/<string:delete_id>')
api.add_resource(LoginAPI, '/login')


if __name__ == '__main__':
    app.run(debug=True)  # !!!REMOVE IN PRODUCTION!!!
