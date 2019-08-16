from api.models import User


def main():
    user = User.query.all()[0]
    return user.username


if __name__ == '__main__':
    print(main())
