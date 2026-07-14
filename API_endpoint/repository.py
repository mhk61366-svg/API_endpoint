from abc import ABC, abstractmethod

class User_Repository(ABC):
    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int):
        pass

    @abstractmethod
    def create_user(self, user_data: dict):
        pass

    @abstractmethod
    def update_user(self, user_id: int, user_data: dict):
        pass

    @abstractmethod
    def delete_user(self, user_id: int):
        pass

class InMemoryUserRepository(User_Repository):
    def __init__(self):
        self.user_data = {
            1 : {"id": 1, "name": "Alice", "age": 30, "email": "alice@gmail.com"},
            2 : {"id": 2, "name": "Bob", "age": 25, "email": "bob@gmail.com"},
            3 : {"id": 3, "name": "Charlie", "age": 35, "email": "charlie@gmail.com"}

            }
    def get_all_users(self):
        return list(self.user_data.values())
    
    def get_user_by_id(self, user_id: int):
        return self.user_data.get(user_id)

    def create_user(self, user_data: dict):
        user_id = user_data["id"]
        self.user_data[user_id] = user_data
        return user_data

    def update_user(self, user_id: int, user_data: dict):
        if user_id in self.user_data:
            self.user_data[user_id].update(user_data)
            return self.user_data[user_id]
        return None

    def delete_user(self, user_id: int):
        return self.user_data.pop(user_id, None)