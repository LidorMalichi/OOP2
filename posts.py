from user import User


class Post:

    def __init__(self, owner: User, kind: str):
        self.user = owner
        self.kind = kind

