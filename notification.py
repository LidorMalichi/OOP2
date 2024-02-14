class Notification:
    def __init__(self, notification_type, sender, content=None):
        self.type = notification_type
        self.sender = sender
        self.content = content


class Observer:
    def __init__(self):
        self.notifications = []

    def update(self, notification: Notification):
        # Handle notifications received by the user.
        if notification.type == "like":
            self.notifications.append(f"{notification.sender} liked your post")
        elif notification.type == "comment":
            self.notifications.append(f"{notification.sender} commented on your post")
        elif notification.type == "new_post":
            self.notifications.append(f"{notification.sender} has a new post")


class Observable:
    def __init__(self):
        self.observers = []
        self.__num_of_observers = 0

    def add_observer(self, observer: Observer):
        self.observers.append(observer)
        self.__num_of_observers += 1

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
        self.__num_of_observers -= 1

    def notify_observers(self, notification: Notification):
        for observer in self.observers:
            observer.update(notification)

    def get_num_of_observers(self):
        return self.__num_of_observers

