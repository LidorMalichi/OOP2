
"""
    This class represents an entity that can be followed by other entities.
    It allows for notifications to be sent to all followers.

    Attributes:
        __followers (list): A list of followers associated with the followable entity.
"""
class followable:
    """
        Initializes a followable object with an empty list of followers.
    """
    def __init__(self):
        self.__followers = []


    """
        Adds a follower to the list of followers if not already present.

        Args:
            follower: An object representing the follower.

        Returns:
            bool: True if follower is added successfully, False otherwise.
    """
    def add_follower(self, follower):
        if follower not in self.__followers:
            self.__followers.append(follower)
            return True
        return False


    """
        Removes a follower from the list of followers if present.

        Args:
            follower: An object representing the follower.

        Returns:
            bool: True if follower is removed successfully, False otherwise.
    """
    def remove_follower(self, follower):
        if follower in self.__followers:
            self.__followers.remove(follower)
            return True
        return False


    """
        Notifies all followers with the given arguments.

        Args:
            *args: Variable number of arguments to be passed to followers' notify methods.
    """
    def notify_followers(self, *args):
        for fol in self.__followers:
            fol.notify(*args)


    """
        Returns the number of followers.

        Returns:
            int: Number of followers.
    """
    def num_of_followers(self):
        return len(self.__followers)


"""
    This class represents an entity that follows other followable entities and receives notifications from them.

    Attributes:
        __name (str): The name of the follower.
        __notifications (list): A list of notifications received by the follower.
"""
class follower:
    """
        Initializes a follower with a given name and an empty list of notifications.

        Args:
            name (str): The name of the follower.
    """
    def __init__(self, name: str):
        self.__notifications = []
        self.__name = name


    """
        Allows the follower to start following a followable entity.

        Args:
            followable: An object representing the followable entity.

        Returns:
            bool: True if the follow operation is successful, False otherwise.
    """
        
    def start_follow(self, followable):
        return followable.add_follower(self)


    """
        Allows the follower to stop following a followable entity.

        Args:
            followable: An object representing the followable entity.

        Returns:
            bool: True if the unfollow operation is successful, False otherwise.
    """
    def stop_follow(self, followable):
        return followable.remove_follower(self)


    """
        Receives notifications from followable entities and adds them to the notification list.

        Args:
            *args: Variable number of arguments representing the notification details.
    """
    def notify(self, *args):
        self.__notifications.append(args[0])
        if any(x in args[0] for x in ["liked" , "commented"]):
            print(f'notification to {self.__name}: {"".join([arg for arg in args])}')
        
    
    """
        Prints all notifications received by the follower.
    """
    def print_notifications(self):
        print(f"{self.__name}'s notifications:")
        for notification in self.__notifications:
            print(notification)