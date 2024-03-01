from typing import List
from follow import followable, follower # Importing followable and follower classes from another module



"""
    Represents a user in a social media system.

    This class inherits functionality from both followable and follower classes,
    allowing users to follow other users and receive notifications.

    Attributes:
        __username (str): The username of the user.
        __password (str): The password of the user.
        __num_of_posts (int): The number of posts published by the user.
        __is_Logged (bool): Indicates whether the user is currently logged in.
"""
class User(followable, follower):
    """
        Initializes a User object with a username, password, and other attributes.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
    """
    def __init__(self, username: str, password: str):
        followable.__init__(self) # Initialize followable properties
        follower.__init__(self, username) # Initialize follower properties
        self.__username = username
        self.__password = password
        self.__num_of_posts = 0
        self.__is_Logged: bool = True


    """
        Returns a string representation of the User object.

        Returns:
            str: A string representation containing username, number of posts, and number of followers.
    """
    def __repr__(self):
        return f"User name: {self.__username}, Number of posts: {self.__num_of_posts}, Number of followers: {self.num_of_followers()}"


    """
        Returns the username of the user.

        Returns:
            str: The username of the user.
    """
    def get_username(self) -> str:
        return self.__username


    """
        Checks if the user is logged in.

        Returns:
            bool: True if the user is logged in, False otherwise.
    """
    def is_logged(self) -> bool:
        return self.__is_Logged


    """Makes the user online."""
    def make_online(self):
        self.__is_Logged = True


    """Makes the user offline."""
    def make_offline(self):
        self.__is_Logged = False


    """
        Returns the password of the user.

        Returns:
            str: The password of the user.
    """
    def get_password(self) -> str:
        return self.__password


    """
        Allows the user to follow another user.

        Args:
            user (User): The user to follow.
    """
    def follow(self, user: 'User'):
        if self.__username != user.get_username() and self.__is_Logged:
            if self.start_follow(user):
                print(f"{self.__username} started following {user.get_username()}")


    """
        Allows the user to unfollow another user.

        Args:
            user (User): The user to unfollow.
    """
    def unfollow(self, user: 'User'):
        if(self.__is_Logged):
            if self.stop_follow(user):
                print(f"{self.__username} unfollowed {user.get_username()}")



    """
        Publishes a post by the user.

        Args:
            *args: Variable number of arguments representing the post details.
        
        Returns:
            Post: The published post object.
    """
    def publish_post(self, *args):
        if(self.__is_Logged):

            if(args[0] == "Text"):
                post = TextPost(self, *args)
        
            if(args[0] == "Image"):
                post = ImagePost(self, *args)
        
            if(args[0] == "Sale"):
                post =  SalePost(self, *args)
        
            self.notify_followers(f"{self.get_username()} has a new post")
            print(post)

            self.__num_of_posts += 1

            return post
        
from posts import *