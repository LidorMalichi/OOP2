from user import User
from follow import followable
import matplotlib.pyplot as plt
from matplotlib import image


class Post(followable):

    def __init__(self, owner: User, kind: str):
        followable.__init__(self)
        self._kind = kind
        self._owner = owner
        self.add_follower(owner)

    def like(self, user: User):
        if self._owner.get_username() != user.get_username():
            self.notify_followers(user.get_username() + " liked your post")

    def comment(self, user: User, comm: str):
        if self._owner.get_username() != user.get_username():
            self.notify_followers(user.get_username() + " commented on your post", ": " + comm)

    
class TextPost(Post):

    def __init__(self, owner: User, kind: str, text: str):
        Post.__init__(self, owner, kind)
        self.__text = text
    
    def __repr__(self) -> str:
        return f'{self._owner.get_username()} published a post:\n"{self.__text}"\n' 
    
class ImagePost(Post):

    def __init__(self, owner: User, kind: str, image_location: str):
        Post.__init__(self, owner, kind)
        self.__image_location = image_location

    def display(self):
        #img = image.imread()
        #plt.imshow()
        print("Shows picture")
    
    def __repr__(self) -> str:
        return f"{self._owner.get_username()} posted a picture\n"
    
class SalePost(Post):
    def __init__(self, owner: User, kind: str, product: str, price: int, location: str):
        Post.__init__(self, owner, kind)
        self.__product = product
        self.__price = price
        self.__location = location
        self.__sold = "For sale!"

    def discount(self, discount: int , passw: str):
        if passw == self._owner.get_password() == passw and self.__sold == "For sale!":
            self.__price *= (1 - discount/100)
            print(f"Discount on {self._owner.get_username()} product! the new price is: {self.__price}")

    def sold(self, passw: str):
        if passw == self._owner.get_password():
            self.__sold = "sold!"
            print(f"{self._owner.get_username()}'s product is sold")
    
    def __repr__(self) -> str:
        return f"{self._owner.get_username()} posted a product for sale:\n{self.__sold} {self.__product}, price: {self.__price}, pickup from: {self.__location}\n"
