import sys
import os

sys.path.append(os.getcwd())
# sys.path.append(os.getcwd() + '\\api')
print(sys.path)
from models import User


# def main():
#     user = User.query.all()[0]
#     return user.username
user = User.query.all()[0]
print(user.username)
# if __name__ == '__main__':
#     print(main())

# import sys
# for p in sys.path:
#     print(p)
