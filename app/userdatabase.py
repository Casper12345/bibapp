
""" This is the user database """


class UserDataBase(object):

    """ UserDataBase class"""

    """ Login Status"""

    login_var = False
    login_name = None
    login_id = None

    """ List over users"""

    users_list = list()

    """ Functions """

    def add_user(self,x):
            """ This is a complete list of users that are added to the library"""
            userdatabase.users_list.append(x)
            #return userdatabase.users_list


    def user_surname(self):
        """ This function returns a list of all user surnames """
        return [i.surname for i in userdatabase.users_list]


    def user_first_name(self):
        """ This function returns a list of all user first names """
        return [i.first_name for i in userdatabase.users_list]

userdatabase = UserDataBase()