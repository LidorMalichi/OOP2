

class User():

    def __init__(self, username, password):
        
        self.__username: str = username
        self.__password: str = password
        self.__num_of_followers = 0