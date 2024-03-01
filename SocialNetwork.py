from user import User


"""
    Represents a social network application.

    This class manages user registration, login, and logout functionalities within the social network.

    Attributes:
        _instance: A class variable to store the instance of the SocialNetwork class.
"""
class SocialNetwork:
    _instance = None  # Class variable to store the instance


    """
        Create a new instance of the SocialNetwork class if it doesn't exist.

        Args:
            name (str): The name of the social network.

        Returns:
            SocialNetwork: The instance of the SocialNetwork class.
    """
    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls._instance.users_dict = {}  # Initialize the users_dict
            cls._instance.name = name
            print(f'The social network {name} was created!')
        return cls._instance


    """
        Add a new user to the social network.

        Args:
            user (User): The user object to be added.
    """
    def __add_user(self, user: User):
        self.users_dict[user.get_username()] = user


    """
        Retrieve a user object based on the provided username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            User: The user object associated with the provided username.
    """
    def get_user(self, username: str) -> User:
        return self.users_dict.get(username, None)


    """
        Register a new user in the social network.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.

        Returns:
            User or None: The newly registered user object if successful, None otherwise.
    """
    def sign_up(self, username: str, password: str):
        # Check if username already exists, and the password length
        if username not in self.users_dict and 4 <= len(password) <= 8:
            user1 = User(username, password)
            self.__add_user(user1)
            return user1


    """
        Log in an existing user to the social network.

        Args:
            username (str): The username of the user attempting to log in.
            password (str): The password of the user attempting to log in.
    """
    def log_in(self, username: str, password: str):
        user = self.users_dict.get(username, None)

        if user is not None and user.get_password() == password:
            user.make_online()
            print (f"{username} connected")


    """
        Log out a logged-in user from the social network.

        Args:
            username (str): The username of the user attempting to log out.
    """
    def log_out(self, username: str):
        user = self.users_dict.get(username, None)
        if user is not None and user.is_logged():
            user.make_offline()
            print(f"{username} disconnected")



    """
        Return a string representation of the SocialNetwork object.

        Returns:
            str: A string containing information about the social network and its users.
    """
    def __repr__(self) -> str:
        deli = "\n"
        return  f'{self.name} social network:\n{"".join([use.__repr__() + deli for use in self.users_dict.values()])}'