from functools import wraps
from api.models import User
import json


def is_admin_user(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.get_user().is_admin:
            return func(request, *args, **kwargs)
        else:
            return f'Access denied', 403
    return wrapper


def login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        print(request.get_request().headers)
        auth_token = request.get_context().get('auth_token')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                return func(request, *args, **kwargs)
            else:
                response = {
                    'status': 'fail',
                    'message': resp
                }
                return json.dumps(response), 401
        else:
            response = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return json.dumps(response), 401
    return wrapper
