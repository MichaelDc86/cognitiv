import requests
import json

url = 'http://localhost:5000/'
url_login = 'http://localhost:5000/login'
url_delete = url + 'user/delete2'
url_create = url  # + 'user1'
data = {
    'username': 'admin',
    'email': 'admin@ya.ru',
    'password': '12345'
}


def main():
    s = requests.session()
    resp_read_all = s.get(url=url).json()
    resp_read_user = s.get(url=url+'user1').json()
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
        'username': 'Vasja1',
        'email': 'vasja1@ya.ru',
        'password': '12345',
        'auth_token': token
    }
    headers = {
        'Authorization': token,
        'logged_in_user': logged_in_user
    }
    resp_create = s.post(url=url_create, data=data_create, headers=headers).json()
    resp_delete = s.delete(url=url_delete, data=data_create, headers=headers).json()

    return resp_read_all, resp_read_user, resp_delete, resp_create


if __name__ == '__main__':
    print(main())
