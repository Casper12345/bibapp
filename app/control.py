# import scripts
import user
import book
import shelf
import userdatabase



class Control(object):

    """ Control class """

    def __init__(self):
        pass

    """ Add Book Methods """

    def add_book_function(self, title, surname, first_name, pub_year):

        m = book.Book(title, surname, first_name, pub_year, None)

        shelf.shelf.add_book(m)

        print shelf.shelf.books_list

        return m

    """ Add User Methods """

    def add_user_function(self, surname, first_name, date_of_birth):

        m = user.User(surname, first_name, date_of_birth, None)

        userdatabase.userdatabase.add_user(m)

        print userdatabase.userdatabase.users_list

        return m

    """ Search Book Methods """

    """ Search by Title Methods """

    def search_book_function_a(self, a):
        search = shelf.shelf.books_title()

        print search

        if a in search:

            list_index = search.index(a)
            book_list = shelf.shelf.books_list
            found_object = book_list[list_index]

            return found_object

        else:
            return False


    def search_book_function_b(self, b):
        search = shelf.shelf.books_surname()

        if b in search:
            list_index = search.index(b)
            book_list = shelf.shelf.books_list
            found_object = book_list[list_index]

            # print book template
            return found_object


        else:
            return False


    def search_book_function_c(self, c):
        search = shelf.shelf.books_first_name()

        if c in search:
            list_index = search.index(c)
            book_list = shelf.shelf.books_list
            found_object = book_list[list_index]

            # print book template
            return found_object


        else:
            return False

    """ Search User Methods """

    def search_user_function_a(self, a):
        search = userdatabase.userdatabase.user_surname()

        if a in search:
            list_index = search.index(a)
            user_list = userdatabase.userdatabase.users_list
            found_object = user_list[list_index]

            # print user template
            return found_object

        else:
            return False


    def search_user_function_b(self, b):
        search = userdatabase.userdatabase.user_first_name()

        if b in search:
            list_index = search.index(b)
            user_list = userdatabase.userdatabase.users_list
            found_object = user_list[list_index]

            # print user template
            return found_object


        else:
            return False

    """ User Login Method """

    """ User Borrow Book Method"""

control = Control()




