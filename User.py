class User:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def __str__(self):
        return f'Login: {self.login}\nPassword: {self.password}'

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(str(password)) >= 8:
            self.__password = password
        else:
            print('Пароль должен содержать 8 и более символов')
