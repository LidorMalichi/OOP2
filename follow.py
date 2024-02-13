

class followable:
    def __init__(self):
        self.__followers = []

    def add_follower(self, follower):
        if follower not in self.__followers:
            self.__followers.append(follower)
            return True
        return False

    def remove_follower(self, follower):
        if follower in self.__followers:
            self.__followers.remove(follower)
            return True
        return False

    def notify_followers(self, *args):
        for fol in self.__followers:
            fol.notify(*args)

    def num_of_followers(self):
        return len(self.__followers)


class follower:
    def __init__(self, name: str):
        self.__notifications = []
        self.__name = name
    
    def start_follow(self, followable):
        return followable.add_follower(self)

    def stop_follow(self, followable):
        return followable.remove_follower(self)

    def notify(self, *args):
        self.__notifications.append(args[0])
        if any(x in args[0] for x in ["liked" , "commented"]):
            print(f'notification to {self.__name}: {"".join([arg for arg in args])}')
        
    
    def print_notifications(self):
        print(f"{self.__name}'s notifications:")
        for notification in self.__notifications:
            print(notification)