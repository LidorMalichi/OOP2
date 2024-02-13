from typing import List
from notification import Notification


class PostFactory:
    @staticmethod
    def create_post(owner: 'User', kind: str, *args):
        if kind == "Sale":
            return SalePost(owner, *args)
        elif kind == "Text":
            return TextPost(owner, *args)
        elif kind == "Image":
            return ImagePost(owner, *args)
        else:
            raise ValueError(f"Invalid post kind: {kind}")


class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.__num_of_posts = 0
        self.__followers = []
        self.__is_online: bool = True
        self.__notifications: List[str] = []

    def __repr__(self):
        return (f"User name: {self.__username}, Number of posts: {self.__num_of_posts}, "
                f"Number of followers: {self.get_num_of_followers()}")

    def get_followers(self):
        return self.__followers

    def get_username(self) -> str:
        return self.__username

    def is_online(self) -> bool:
        return self.__is_online

    def make_online(self):
        self.__is_online = True

    def make_offline(self):
        self.__is_online = False

    def get_password(self) -> str:
        return self.__password

    def get_num_of_followers(self) -> int:
        return len(self.__followers)

    def follow(self, user: 'User'):
        user.add_follower(self)

    def unfollow(self, unfollower: 'User'):
        unfollower.remove_follower(self)

    def add_follower(self, follower: 'User'):
        if follower not in self.__followers:
            print(f"{follower.get_username()} started following {self.__username}")
            self.__followers.append(follower)

    def remove_follower(self, unfollower: 'User'):
        if unfollower in self.__followers:
            print(f"{unfollower.get_username()} unfollowed {self.__username}")
            self.__followers.remove(unfollower)

    def print_notifications(self):
        print(f"{self.__username}'s notifications:")
        for notification in self.__notifications:
            print(notification)

    def update(self, notification):
        if notification.type == "like":
            self.__notifications.append(f"{notification.sender} liked your post")
        elif notification.type == "comment":
            self.__notifications.append(f"{notification.sender} commented on your post")
        elif notification.type == "new_post":
            self.__notifications.append(f"{notification.sender} has a new post")

    def notify_followers(self, notification_type):
        for follower in self.__followers:
            notification = Notification(notification_type, self.get_username())
            follower.update(notification)

    def publish_post(self, kind: str, *args):
        post = PostFactory.create_post(self, kind, *args)
        print(post)
        self.notify_followers("new_post")
        self.__num_of_posts += 1
        return post


from posts import ImagePost, SalePost, TextPost
