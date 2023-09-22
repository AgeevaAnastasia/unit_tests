class User:
    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password
        self._is_authenticate = False

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @property
    def is_authenticate(self):
        return self._is_authenticate

    def authenticate(self, login: str, password: str) -> bool:
        self._is_authenticate = self._login == login and self._password == password
        return self._is_authenticate
