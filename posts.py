from notification import Notification
from user import User
import matplotlib.pyplot as plt
import matplotlib.image as img


class Post:
    """
        Represents a generic post in a social network.

        Design Pattern:
        - Observer Pattern: Users are observers to their own posts, and notifications are sent to the post owner.

        Attributes:
        - owner (User): The user who owns the post.
        - kind (str): The type of the post (e.g., "text", "image", "sale").

        Methods:
        - like(liker: User): Allow a user to like the post, sending a notification to the post owner.
        - comment(commenter: User, text: str): Allow a user to comment on the post,
          sending a notification to the post owner.
        """
    def __init__(self, owner: User, kind: str):
        self.owner = owner
        self.kind = kind

    def like(self, liker: User):
        if self.owner.get_username() != liker.get_username():
            notification = Notification("like", liker.get_username())
            self.owner.update(notification)
            print(f"notification to {self.owner.get_username()}: "
                  f"{liker.get_username()} liked your post")

    def comment(self, commenter: User, text: str):
        if self.owner.get_username() != commenter.get_username():
            notification = Notification("comment", commenter.get_username())
            self.owner.update(notification)
            print(f"notification to {self.owner.get_username()}: "
                  f"{commenter.get_username()} commented on your post: {text}")


class SalePost(Post):
    """
       Represents a post about a product for sale.

       Attributes:
       - product (str): The name of the product.
       - price (float): The price of the product.
       - pick_up_location (str): The location for picking up the product.
       - available (str): The availability status of the product ("For sale!" or "Sold!").

       Methods:
       - sold(password: str): Mark the product as sold.
       - discount(percent: int, password: str): Apply a discount to the product price.
       """
    def __init__(self, owner: 'User', *args):
        super().__init__(owner, kind="sale")
        self.product, self.price, self.pick_up_location = args
        self.price = self.price
        self.available = "For sale!"

    def sold(self, password: str) -> None:
        if self.owner.get_password() == password and self.available == "For sale!":
            self.available = "Sold!"
            print(f"{self.owner.get_username()}'s product is sold")

    def discount(self, percent: int, password: str) -> None:
        if self.available == "For sale!" and self.owner.get_password() == password:
            self.price = float(self.price)
            self.price *= (1 - percent / 100)
            print(f"Discount on {self.owner.get_username()} product! the new price is: {self.price}")

    def __repr__(self):
        return (f"{self.owner.get_username()} posted a product for sale:"
                f"\n{self.available} {self.product}, price: {self.price}, "
                f"pickup from: {self.pick_up_location}\n")


class ImagePost(Post):
    """
       Represents a post containing an image.

       Attributes:
       - image_path (str): The file path of the image.

       Methods:
       - display(): Display the image.
       """
    def __init__(self, owner: 'User', *args):
        super().__init__(owner, kind="image")
        self.image_path, = args

    def display(self):
        image = img.imread(self.image_path)
        plt.imshow(image)
        print("Shows picture")

    def __repr__(self):
        return f"{self.owner.get_username()} posted a picture\n"


class TextPost(Post):
    """
        Represents a text-based post.

        Attributes:
        - text_content (str): The content of the text post.
        """
    def __init__(self, owner: 'User', *args):
        super().__init__(owner, kind="text")
        self.text_content, = args

    def __repr__(self):
        return (f"{self.owner.get_username()} published a post:"
                f"\n\"{self.text_content}\"\n")
