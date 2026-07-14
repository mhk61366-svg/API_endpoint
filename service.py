class UserService:
    def __init__(self, repository):
        self.repo = repository

    def get_all_users(self):
        return self.repo.get_all_users()

    def get_user_by_id(self, user_id: int):
        return self.repo.get_user_by_id(user_id)

    def create_user(self, user_data: dict):
        return self.repo.create_user(user_data)

    def update_user(self, user_id: int, user_data: dict):
        return self.repo.update_user(user_id, user_data)
    
    def delete_user(self, user_id: int):
        return self.repo.delete_user(user_id)
    
