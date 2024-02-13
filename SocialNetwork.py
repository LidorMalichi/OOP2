from typing import Any
from user import User


class SocialNetwork:
    """
    Represents a simple social network where users can sign up, log in, and interact with each other.

    Design Pattern:
    - Singleton Pattern: Ensures that only one instance of the social network exists.
    - Observer Pattern: Users act as both subjects (observed) and observers (observing their own posts).

    Attributes:
    - _instance (SocialNetwork): Class variable to store the instance of the social network.
    - users_list (List[User]): List to store registered users.
    - name (str): Name of the social network.

    Methods:
    - get_user(username: str) -> User | None: Retrieve a user by username.
    - sign_up(username: str, password: str) -> User | None: Register a new user with a unique username.
    - log_in(username: str, password: str): Log in a user by setting their online status.
    - log_out(username: str): Log out a user by setting their offline status.
    - __repr__() -> str: Returns a string representation of the social network, including user details.
    """

    _instance = None

    def __new__(cls, name):
        """
        Create a new instance of the social network if it doesn't already exist.

        Parameters:
        - name (str): Name of the social network.

        Returns:
        - SocialNetwork: Instance of the social network.
        """
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls._instance.users_list = []
            cls._instance.name = name
            print(f"The social network {cls._instance.name} was created!")
        return cls._instance

    def get_user(self, username: str) -> Any | None:
        """
        Retrieve a user by their username.

        Parameters:
        - username (str): Username of the user to retrieve.

        Returns:
        - User | None: The user if found, otherwise None.
        """
        for user in self.users_list:
            if user.get_username() == username:
                return user
        return None

    def sign_up(self, username: str, password: str):
        """
        Register a new user with a unique username and password.

        Parameters:
        - username (str): Desired username for the new user.
        - password (str): Password for the new user.

        Returns:
        - User | None: The newly registered user if successful, otherwise None.
        """
        # Check if username already exists and password length is within a valid range
        if self.get_user(username) is None and 4 <= len(password) <= 8:
            user1 = User(username, password)
            self.users_list.append(user1)
            return user1

    def log_in(self, username: str, password: str):
        """
        Log in a user by setting their online status.

        Parameters:
        - username (str): Username of the user to log in.
        - password (str): Password for the user.

        Prints:
        - str: A message indicating whether the login was successful.
        """
        user = self.get_user(username)
        if user is not None and user.get_password() == password:
            user.make_online()
            print(f"{username} connected")

    def log_out(self, username: str):
        """
        Log out a user by setting their offline status.

        Parameters:
        - username (str): Username of the user to log out.

        Prints:
        - str: A message indicating whether the logout was successful.
        """
        user = self.get_user(username)
        if user is not None and user.is_online():
            user.make_offline()
            print(f"{username} disconnected")

    def __repr__(self):
        """
        Returns a string representation of the social network, including user details.

        Returns:
        - str: String representation of the social network.
        """
        users_repr = "\n".join([user.__repr__() for user in self.users_list])
        return f"{self.name} social network:\n{users_repr}\n"
