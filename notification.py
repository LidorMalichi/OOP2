class Notification:
    def __init__(self, notification_type, sender, content=None):
        self.type = notification_type
        self.sender = sender
        self.content = content
