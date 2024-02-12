from typing import List


class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.__num_of_followers = 0
        self.__num_of_posts = 0
        self.__followers = []
        self.__is_Logged: bool = True
        self.__notifications: List[str] = []
    def __repr__(self):
        return f"User name: {self.__username}, Number of posts: {self.__num_of_posts}, Number of followers: {self.__num_of_followers}"

    def get_username(self) -> str:
        return self.__username

    def is_logged(self) -> bool:
        return self.__is_Logged

    def make_online(self):
        self.__is_Logged = True

    def make_offline(self):
        self.__is_Logged = False

    def get_password(self) -> str:
        return self.__password

    def get_num_of_followers(self) -> int:
        return self.__num_of_followers

    def follow(self, user: 'User'):
        user.add_follower(self)

    def unfollow(self, unfollower: 'User'):
        unfollower.remove_follower(self)

    def add_follower(self, follower: 'User'):
        if follower not in self.__followers:
            print(f"{follower.get_username()} started following {self.__username}")
            self.__followers.append(follower)
            follower.increment_followers()

    def remove_follower(self, unfollower: 'User'):
        if unfollower in self.__followers:
            print(f"{unfollower.get_username()} unfollowed {self.__username}")
            self.__followers.remove(unfollower)
            unfollower.decrement_followers()

    def increment_followers(self):
        self.__num_of_followers += 1

    def decrement_followers(self):
        self.__num_of_followers -= 1

    def add_notification(self, notification: str):
        self.__notifications.append(notification)

    def print_notifications(self):
        for notification in self.__notifications:
            print(notification)