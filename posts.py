from user import User
from follow import followable
import matplotlib.pyplot as plt
from matplotlib import image



"""
    Represents a generic post in a social media system.

    This class inherits functionality from the followable class,
    allowing posts to have followers and receive notifications.

    Attributes:
        _kind (str): The type of the post.
        _owner (User): The owner of the post.
"""
class Post(followable):

    """
        Initializes a Post object with an owner and kind.

        Args:
            owner (User): The user who owns the post.
            kind (str): The type of the post.
    """
    def __init__(self, owner: User, kind: str):
        followable.__init__(self) # Initialize followable properties
        self._kind = kind
        self._owner = owner
        self.add_follower(owner)


    """
        Allows a user to like the post.

        Args:
            user (User): The user who is liking the post.
    """
    def like(self, user: User):
        if self._owner.get_username() != user.get_username():
            self.notify_followers(user.get_username() + " liked your post")


    """
        Allows a user to comment on the post.

        Args:
            user (User): The user who is commenting on the post.
            comm (str): The comment text.
    """
    def comment(self, user: User, comm: str):
        if self._owner.get_username() != user.get_username():
            self.notify_followers(user.get_username() + " commented on your post", ": " + comm)



"""
    Represents a text-based post in a social media system.

    This class inherits functionality from the Post class,
    allowing users to publish text-based posts.
"""
class TextPost(Post):

    """
        Initializes a TextPost object with an owner, kind, and text.

        Args:
            owner (User): The user who owns the post.
            kind (str): The type of the post.
            text (str): The text content of the post.
    """
    def __init__(self, owner: User, kind: str, text: str):
        Post.__init__(self, owner, kind)
        self.__text = text


    """
        Returns a string representation of the TextPost object.

        Returns:
            str: A string representation containing the username of the owner and the text content of the post.
    """
    def __repr__(self) -> str:
        return f'{self._owner.get_username()} published a post:\n"{self.__text}"\n' 


"""
    Represents an image-based post in a social media system.

    This class inherits functionality from the Post class,
    allowing users to publish image-based posts.
"""
class ImagePost(Post):

    """
        Initializes an ImagePost object with an owner, kind, and image location.

        Args:
            owner (User): The user who owns the post.
            kind (str): The type of the post.
            image_location (str): The location of the image file.
    """
    def __init__(self, owner: User, kind: str, image_location: str):
        Post.__init__(self, owner, kind)
        self.__image_location = image_location


    """
        Displays the image associated with the ImagePost.
    """
    def display(self):
       
        image1 = image.imread(self.__image_location)
        plt.imshow(image1)
        plt.title('Loaded Image')
        plt.axis("off")
        plt.show()
        print("Shows picture")
    

    """
        Returns a string representation of the ImagePost object.

        Returns:
            str: A string representation containing the username of the owner and an indication that the post is an image.
    """
    def __repr__(self) -> str:
        return f"{self._owner.get_username()} posted a picture\n"


"""
    Represents a sale post in a social media system.

    This class inherits functionality from the Post class,
    allowing users to publish sale posts.
"""   
class SalePost(Post):

    """
        Initializes a SalePost object with an owner, kind, product, price, and location.

        Args:
            owner (User): The user who owns the post.
            kind (str): The type of the post.
            product (str): The product being sold.
            price (int): The price of the product.
            location (str): The pickup location for the product.
    """
    def __init__(self, owner: User, kind: str, product: str, price: int, location: str):
        Post.__init__(self, owner, kind)
        self.__product = product
        self.__price = price
        self.__location = location
        self.__sold = "For sale!"


    """
        Applies a discount to the product price.

        Args:
            discount (int): The discount percentage.
            passw (str): The password of the owner for verification.
    """
    def discount(self, discount: int , passw: str):
        if passw == self._owner.get_password() == passw and self.__sold == "For sale!" and self._owner.is_logged():
            self.__price *= (1 - discount/100)
            print(f"Discount on {self._owner.get_username()} product! the new price is: {self.__price}")


    """
        Marks the product as sold.

        Args:
            passw (str): The password of the owner for verification.
    """
    def sold(self, passw: str):
        if passw == self._owner.get_password() and self._owner.is_logged():
            self.__sold = "Sold!"
            print(f"{self._owner.get_username()}'s product is sold")


    """
        Marks the product as sold.

        Args:
            passw (str): The password of the owner for verification.
    """
    def __repr__(self) -> str:
        return f"{self._owner.get_username()} posted a product for sale:\n{self.__sold} {self.__product}, price: {self.__price}, pickup from: {self.__location}\n"
