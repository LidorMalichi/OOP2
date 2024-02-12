from user import User
from notification import Notification


class Post:

    def __init__(self, owner: User, kind: str):
        self.owner = owner
        self.kind = kind

    def like(self, liker: User):
        if self.owner.get_username() != liker.get_username():
            notification = Notification("like", liker.get_username())
            self.owner.update(notification)
            print(f"Notification to {self.owner.get_username()}: "
                  f"{liker.get_username()} liked your post.")

    def comment(self, commenter: User, text: str):
        if self.owner.get_username() != commenter.get_username():
            notification = Notification("comment", commenter.get_username())
            self.owner.update(notification)
            print(f"Notification to {self.owner.get_username()}: "
                  f"{commenter.get_username()} commented on your post: {text}")


class SalePost(Post):
    def __init__(self, owner: 'User', *args):
        super().__init__(owner, kind="sale")
        self.product, self.price, self.pick_up_location = args
        self.price = float(self.price)
        self.available = "for sale!"

    def sold(self, password: str) -> None:
        if self.owner.get_password() == password and self.available=="for sale!":
            self.available = "sold!"
            print(f"{self.owner.get_username()}'s product is sold.")

    def discount(self, percent: int, password: str) -> None:
        if self.available =="for sale!" and self.owner.get_password() == password:
            self.price *= (1 - percent / 100)
            print(f"discount on {self.owner.get_username()} product! the new price is:{self.price}")

    def __repr__(self):
        return (f"{self.owner.get_username()} posted a product for sale:"
                f"\n{self.available} {self.product}, price: {self.price}, "
                f"pickup from: {self.pick_up_location}")


class ImagePost(Post):
    def __init__(self, owner: 'User', *args):
        super().__init__(owner, kind="image")
        self.image_path, = args

    def display(self):
        return

    def __repr__(self):
        return f"{self.owner.get_username()} posted a picture"


class TextPost(Post):

    def __init__(self, owner: 'User', *args):
        super().__init__(owner, kind="text")
        self.text_content, = args

    def __repr__(self):
        return (f"{self.owner.get_username()} published a post: "
                f"\n{self.text_content}")
