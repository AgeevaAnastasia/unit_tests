class User:
    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password
        self._authorized = False
        self.admin = False

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @property
    def authorized(self):
        return self._authorized

    def auth(self, login: str, password: str) -> bool:
        if self._login == login and self._password == password:
            self._authorized = True
            return True
        return False

    def __str__(self):
        return f'{self.login}, {self.password}, {self.authorized}, {self.admin}'


class UserRepository:
    def __init__(self):
        self.repository = []

    def add_user(self, user: User):
        if user.authorized:
            self.repository.append(user)
            # Если это единственный пользователь репозитория, то делаем его админом
            if len(self.repository) == 1:
                user.admin = True

    def set_admin(self, user_master: User, user_slave: User):
        if user_master in self.repository and user_slave in self.repository:
            if user_master.admin:
                user_slave.admin = True

    def logout_all_no_admins(self, user_initiator: User):
        # если инициатор - пользователь-админ
        if user_initiator.admin:
            # удаляем из репозитория всех неадминов
            for user in self.repository:
                if not user.admin:
                    self.repository.remove(user)

    def __str__(self):
        return '\n'.join([str(user) for user in self.repository])


if __name__ == '__main__':
    user_1 = User('login_1', 'password_1')
    user_2 = User('login_2', 'password_2')
    user_repository = UserRepository()
    user_1.auth(user_1.login, user_1.password)
    user_repository.add_user(user_1)
    user_2.auth(user_2.login, user_2.password)
    user_repository.add_user(user_2)

    # user_2 пытается сделать user_1 админом, но у него это не получается, т.к. он сам не админ
    user_repository.set_admin(user_2, user_1)
    # user_1 делает админом user_2
    # user_repository.set_admin(user_1, user_2)

    print(user_repository)

    user_repository.logout_all_no_admins(user_1)
    print(user_repository)
