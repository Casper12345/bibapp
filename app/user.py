# import script
import userdatabase


class User(object):

    """ User class """

    def __init__(self, surname, first_name, date_of_birth, password, borrowed_books):
        self.surname = surname
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.password = password
        self.borrowed_books = borrowed_books
        self.borrowed_books = list()

    def borrowed_books(self, book):
        """ This method shows what books a user has borrowed"""
        self.borrowed_books.append(book)

    #def login_user(self):
     #   """ This method logs in the user """
      #  userdatabase.UserDataBase.login_id = self
       # userdatabase.UserDataBase.login_name = (self.surname, self.first_name)







