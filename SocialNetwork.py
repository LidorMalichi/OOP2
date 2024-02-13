from user import User


class SocialNetwork:
    _instance = None  # Class variable to store the instance

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls._instance.users_dict = {}  # Initialize the users_dict
            cls._instance.name = name
        return cls._instance

    def __add_user(self, user: User):
        self.users_dict[user.get_username()] = user

    def get_user(self, username: str) -> User:
        return self.users_dict.get(username, None)

    def sign_up(self, username: str, password: str):
        # Check if username already exists, and the password length
        if username not in self.users_dict and 4 <= len(password) <= 8:
            user1 = User(username, password)
            self.__add_user(user1)
            return user1

    def log_in(self, username: str, password: str):
        user = self.users_dict.get(username, None)

        if user is not None and user.get_password() == password:
            user.make_online()
            print (f"{username} connected\n")

    def log_out(self, username: str):
        user = self.users_dict.get(username, None)
        if user is not None and user.is_logged():
            user.make_offline()
            print(f"{username} disconnected\n")


    def __repr__(self) -> str:
        deli = "\n"
        return  f'{self.name} social network:\n\n{"".join([use.__repr__() + deli for use in self.users_dict.values()])}'