
class Book(object):

    """ Books class """

    def __init__(self, title, author_sur, author_first, pub_year, user_name):
        self.title = title
        self.author_sur = author_sur
        self.author_first = author_first
        self.pub_year = pub_year
        self.user_name = user_name

    def vacancy_status(self, status):
        """ This method shows the books vacancy status"""
        self.user_name = status
        return self.user_name









