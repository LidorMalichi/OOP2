from typing import Any

from user import User


class SocialNetwork:
    _instance = None  # Class variable to store the instance

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls._instance.users_list = []
            cls._instance.name = name
            print(f"The social network {cls._instance.name} was created!")
        return cls._instance

    def get_user(self, username: str) -> Any | None:
        for user in self.users_list:
            if user.get_username() == username:
                return user
        return None

    def sign_up(self, username: str, password: str):
        # Check if username already exists, and the password length
        if self.get_user(username) is None and 4 <= len(password) <= 8:
            user1 = User(username, password)
            self.users_list.append(user1)
            return user1

    def log_in(self, username: str, password: str):
        user = self.get_user(username)
        if user is not None and user.get_password() == password:
            user.make_online()
            print(f"{username} connected")

    def log_out(self, username: str):
        user = self.get_user(username)
        if user is not None and user.is_online():
            user.make_offline()
            print(f"{username} disconnected")

    def __repr__(self):
        users_repr = "\n".join([user.__repr__() for user in self.users_list])
        return f"{self.name} Social Network:\n{users_repr}"
