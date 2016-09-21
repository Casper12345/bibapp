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

        m = book.Book(title, surname, first_name, pub_year, (None, None), None, 'Available')

        shelf.shelf.add_book(m)

        print shelf.shelf.books_list

        return m

    """ Add User Methods """

    def add_user_function(self, surname, first_name, date_of_birth, password):

        m = user.User(surname, first_name, date_of_birth, password, [])

        userdatabase.userdatabase.add_user(m)

        print userdatabase.userdatabase.users_list

        return m

    """ Search Book Methods """

    """ Search by Title Methods """


    def search_book_function_a(self, a):
        search = shelf.shelf.books_title()

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

    """ User Login Methods"""

    """ Password Match """

    def password_match(self, sur_name, password):

        sur_name_list = userdatabase.userdatabase.user_surname()

        if sur_name in sur_name_list:

            list_index = sur_name_list.index(sur_name)
            password_list = userdatabase.userdatabase.user_password()
            found_object = password_list[list_index]

            if found_object == password:
                return True

            else:
                return False

        return False

    """ User Login """


    def login(self, sur_name):

        sur_name_list = userdatabase.userdatabase.user_surname()

        list_index = sur_name_list.index(sur_name)
        users_list = userdatabase.userdatabase.users_list
        user_object = users_list[list_index]

        # set login name and login id
        userdatabase.userdatabase.login_id = user_object
        userdatabase.userdatabase.login_name = (user_object.surname, user_object.first_name)
        print userdatabase.userdatabase.login_id
        print userdatabase.userdatabase.login_name

    """ User Borrow Book Method"""

    # book object
    book_object_user = None

    def borrow_book(self):
        if control.book_object_user.av_status == 'Available':
            book.Book.vacancy_status(control.book_object_user, userdatabase.userdatabase.login_id)
            user.User.borrowed_books(userdatabase.userdatabase.login_id, control.book_object_user)
            book.Book.av_status_not_available(control.book_object_user)

        else:
            return

    """  Return Book Method """

    book_object_return = None

    def return_book(self):
        m = book.Book.av_status_available(control.book_object_return)
        user.User.return_books(m)
        control.book_object_return.user_id = None


control = Control()




