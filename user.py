
from notification import Notification, Observer, Observable


class PostFactory:
    """
       Factory class responsible for creating different types of posts.

       Design Pattern:
       - Factory Method Pattern: Provides an interface for creating posts, allowing subclasses to alter
       the type of posts that will be created.

       Methods:
       - create_post(owner: 'User', kind: str, *args) -> Post: Create a post of the specified kind
       with the given arguments.
       """

    @staticmethod
    def create_post(creator, kind: str, *args):
        post_types = {"Sale": SalePost, "Text": TextPost, "Image": ImagePost}
        if kind in post_types:
            return post_types[kind](creator, *args)
        else:
            raise ValueError(f"Invalid post kind: {kind}")


class User(Observer, Observable):
    """
        Represents a user in a social network.

        Design Pattern:
        - Observer Pattern: Users act as observers to their own posts, receiving notifications when their
          posts are liked, commented, or when they have new posts.
        - Subject Pattern: Each user acts as a subject, notifying their followers when they publish a new post.

        Attributes:
        - __username (str): The username of the user.
        - __password (str): The password of the user.
        - __num_of_posts (int): The number of posts published by the user.
        - __followers (List[User]): List of users who follow the current user.
        - __is_online (bool): The online status of the user.
        - __notifications (List[str]): List of notifications received by the user.
        - __observers (List[User]): List of users observing the current user.
        """

    def __init__(self, username: str, password: str):
        Observer.__init__(self)  # Call Observer's constructor
        Observable.__init__(self)  # Call Observable's constructor
        self.__username = username
        self.__password = password
        self.__num_of_posts = 0
        self.__is_online: bool = True

    def __repr__(self):
        return (f"User name: {self.__username}, Number of posts: {self.__num_of_posts}, "
                f"Number of followers: {self.get_num_of_followers()}")

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
        return self.get_num_of_observers()

    def follow(self, user: 'User'):
        if self not in user.observers:
            print(f"{self.get_username()} started following {user.__username}")
            user.add_observer(self)

    def unfollow(self, to_un_follow: 'User'):
        if self in to_un_follow.observers:
            print(f"{self.get_username()} unfollowed {to_un_follow.__username}")
            to_un_follow.remove_observer(self)

    def print_notifications(self):
        print(f"{self.__username}'s notifications:")
        for notification in self.notifications:
            print(notification)

    def publish_post(self, kind: str, *args):
        # Publish a post of the specified kind and notify followers.
        post = PostFactory.create_post(self, kind, *args)
        print(post)
        notification = Notification("new_post", self.get_username())
        self.notify_observers(notification)
        self.__num_of_posts += 1
        return post


from posts import ImagePost, SalePost, TextPost
