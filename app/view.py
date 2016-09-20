# import from scripts


class View(object):

    """ View class """

    """ Ask function menu"""


    def ask_action_1(self):
        return raw_input('Select action: ').lower()


    """ Ask functions Add Book """


    def ask_action_2(self):
        return raw_input('Title of Book: ').capitalize()


    def ask_action_3(self):
        return raw_input('Surname of Author: ').capitalize()


    def ask_action_4(self):
        return raw_input('First Name of Author: ').capitalize()


    def ask_action_5(self):
        return raw_input('Publishing Year: ')


    """ Ask functions Add User """


    def ask_action_6(self):
        return raw_input('Surname of User: ').capitalize()


    def ask_action_7(self):
        return raw_input('First Name of User: ').capitalize()


    def ask_action_8(self):
        return raw_input('Date of Birth: ')


    """ Ask Functions Search Title"""


    def ask_action_9(self):
        return raw_input('Enter Title: ')


    def ask_action_10(self):
        return raw_input('Enter Surname: ')


    def ask_action_11(self):
        return raw_input('Enter First Name: ')


    """ Ask Function Borrow Book """


    def ask_action_12(self):
        return raw_input('Do you want to borrow the book(Y/N): ').lower()


    """ Ask Function Login User """


    def ask_action_13(self):
        return raw_input('Do you want to login user(Y/N): ').lower()


    """ Menu functions"""


    def menu_function_1(self):
        menu_1 = ('Add Book(AB)', 'Add User(AU)','Search Book(SB)','Search User(SU)','Quit(Q)')
        return menu_1


    def menu_function_2(self):
        menu_2 = ('Search by Title(ST)', 'Search by Author Surname(SS)', 'Search by Author First Name(SF)', 'Main Menu(M)')
        return menu_2


    def menu_function_3(self):
        menu_3 = ('Search by Surname(SS)', 'Search by First Name(SF)')
        return menu_3


    """ Menu Output Methods"""


    def menu_output_1(self):
        menu_1 = self.menu_function_1()
        for i in menu_1:
            print i
        print '\n'


    def menu_output_2(self):
        menu_2 = self.menu_function_2()
        for i in menu_2:
            print i
        print '\n'


    def menu_output_3(self):
        menu_3 = self.menu_function_3()
        for i in menu_3:
            print i
        print '\n'


    """ Templates Output Functions """

    def book_template(self, title, surname, first_name, pub_year, status):
        if status is None:
            av_status = 'Available'

        else:
            av_status = 'Not available'

        print '\n'*3
        print 'Title: {}'.format(title)
        print '\n'
        print 'Author: {}, {}'.format(surname, first_name)
        print '\n'
        print 'Publishing Year: {}'.format(pub_year)
        print '\n'
        print 'Availability Status: {}'.format(av_status)
        print 'Borrowed by: {}'.format(status)
        print '\n'*2

    def user_template(self,surname, first_name, date_of_birth, books):
        print '\n'*3
        print 'User: {}, {}'.format(surname, first_name)
        print '\n'
        print 'Date of Birth: {}'.format(date_of_birth)
        print '\n'
        print 'Books Borrowed: {}'.format(books)
        print '\n' * 2


    """ Auxiliary Output Functions """

    def try_again_print(self):
        print 'Try Again'


    def not_found(self):
        print 'Not Found'


    def user_logged_in(self, surname, first_name):
        print '{}, {} Logged In'.format(surname, first_name)


view = View()
