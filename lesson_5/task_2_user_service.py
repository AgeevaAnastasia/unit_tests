from task_2_user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_user_name(self, user_id: int) -> str:
        return self._user_repository.get_user_by_id(user_id)
