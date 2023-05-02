# Уровень 1
import json

login = input('введите логин: ')
password = input('введите пароль: ')


def register(login: str, passwd: str):
    with open('db.json', 'a', encoding='utf8') as f:
        json.dump(obj={'login': login, 'password': passwd}, sort_keys=False,
                  indent=4, ensure_ascii=False, separators=(',', ': '), fp=f)


register(login, password)

# Уровень 2


def is_exists(login: str):
    with open('db.json', 'r', encoding='utf8') as f:
        if json.load(f)['login'] == login:
            print('такой пользователь существует')
        else:
            print('такой пользователь НЕ существует')


is_exists('f')

# Уровень 3


def login_function(login: str, passwd: str):
    with open('db.json', 'r', encoding='utf8') as f:
        data = json.load(f)

        if data['login'] == login and data['password'] == passwd:
            print('вы успешно авторизовались')
        else:
            print('введен неправильный логин или пароль, попробуйте еще раз')


login_function('user', '123')
