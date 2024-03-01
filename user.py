from typing import List
from follow import followable, follower


class User(followable, follower):
    def __init__(self, username: str, password: str):
        followable.__init__(self)
        follower.__init__(self, username)
        self.__username = username
        self.__password = password
        self.__num_of_posts = 0
        self.__is_Logged: bool = True

    def __repr__(self):
        return f"User name: {self.__username}, Number of posts: {self.__num_of_posts}, Number of followers: {self.num_of_followers()}"

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

    def follow(self, user: 'User'):
        if self.__username != user.get_username() and self.__is_Logged:
            if self.start_follow(user):
                print(f"{self.__username} started following {user.get_username()}")

    def unfollow(self, user: 'User'):
        if(self.__is_Logged):
            if self.stop_follow(user):
                print(f"{self.__username} unfollowed {user.get_username()}")


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