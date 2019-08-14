import requests
import json

from api.models import User

url = 'http://localhost:5000/'
url_login = 'http://localhost:5000/login'
url_create = url
data = {
    'username': 'admin',
    'email': 'admin@ya.ru',
    'password': '12345'
}


def test_get():
    s = requests.session()
    resp = s.get(url=url).json()
    assert resp == {'users': [{'1': 'admin'}]}


def test_create():
    s = requests.session()
    response = s.post(url=url_login, data=data).json()

    try:
        dict_resp = json.loads(response)
        token = dict_resp.get('auth_token')
        logged_in_user = dict_resp.get('user_id')
    except TypeError:
        token = response.get('auth_token')
        logged_in_user = response.get('user_id')
    print(token)
    data_create = {
        'username': 'Vasja11',
        'email': 'vasja11@ya.ru',
        'password': '12345',
        'auth_token': token
    }
    headers = {
        'Authorization': token,
        'logged_in_user': logged_in_user
    }
    resp = s.post(url=url_create, data=data_create, headers=headers).json()
    cur_user = User.query.filter_by(username=data_create['username']).first()
    ans = {
        "status": "success",
        "message": "Successfully created!",
        "auth_token": json.loads(resp)['auth_token'],
        "id_user_created": cur_user.id
    }
    url_delete = url + 'user/delete/' + str(cur_user.id)
    resp_del = s.delete(url=url_delete, data=data_create, headers=headers).json()
    assert resp == json.dumps(ans)


def test_delete():
    s = requests.session()
    response = s.post(url=url_login, data=data).json()

    try:
        dict_resp = json.loads(response)
        token = dict_resp.get('auth_token')
        logged_in_user = dict_resp.get('user_id')
    except TypeError:
        token = response.get('auth_token')
        logged_in_user = response.get('user_id')
    print(token)
    data_create = {
        'username': 'Vasja33',
        'email': 'vasja33@ya.ru',
        'password': '12345',
        'auth_token': token
    }
    headers = {
        'Authorization': token,
        'logged_in_user': logged_in_user
    }
    resp_create = s.post(url=url_create, data=data_create, headers=headers).json()
    user = User.query.filter_by(username=data_create['username']).first()
    url_delete = url + 'user/delete/' + str(user.id)
    resp = s.delete(url=url_delete, data=data_create, headers=headers).json()

    ans = f'User {user} was deleted!'

    assert resp == ans


def test_login():
    s = requests.session()
    response = s.post(url=url_login, data=data).json()
    ans = json.loads(response)['message']

    assert ans == 'Successfully logged in.'
