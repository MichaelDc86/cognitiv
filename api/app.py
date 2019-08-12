from flask import Flask, jsonify
from flask_restful import Resource, Api

from api import app
api = Api(app)

from api.models import User
from api import db


class UserCrud(Resource):

    def get(self):
        users_list = []
        users = User.query.all()
        for user in users:
            users_list.append({user.id: user.username})
        return jsonify({'users': users_list})

    # def put(self, user_id):
    #     todos[todo_id] = request.form['data']
    #     return {todo_id: todos[todo_id]}

    def post(self):
        new_user = User(username='Ivan1', email='asdas@ya.ru')
        db.session.add(new_user)
        db.session.commit()
        return jsonify(f'user {new_user} was created!')


api.add_resource(UserCrud, '/')


# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)  # !!!REMOVE IN PRODUCTION!!!
