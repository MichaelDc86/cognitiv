from flask import jsonify, request
from flask_restful import Resource, Api

from api import app

from api.models import User
from api import db

api = Api(app)


class UserCrud(Resource):

    def get(self, user_id=None):
        users_list = []
        # print(f'user_id-------------------WWW{user_id}WWW')
        # if user_id and user_id != 'favicon.ico':
        #     users = User.query.filter_by(id=int(user_id[-1::])).first()
        #     return jsonify({'users': users.username})
        # else:
        #     users = User.query.all()
        #     for user in users:
        #         users_list.append({user.id: user.username})
        #         return jsonify({'users': users_list})
        users = User.query.all()
        for user in users:
            print(user.email)
            users_list.append({user.id: user.username})
            return jsonify({'users': users_list})

    # def put(self, user_id):
    #     # todos[todo_id] = request.form['data']
    #     user = User.query.filter_by(id=int(user_id[-1::])).first()
    #     print(user)
    #     print(request.form)
    #     print(request.form['data'])
    #     # return {todo_id: todos[todo_id]}

    # def post(self):
    #     new_user = User(username='Ivan1', email='asdas@ya.ru')
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return jsonify(f'user {new_user} was created!')


api.add_resource(UserCrud, '/')  # , '/<string:user_id>')


# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': 1234})


if __name__ == '__main__':
    app.run(debug=True)  # !!!REMOVE IN PRODUCTION!!!
