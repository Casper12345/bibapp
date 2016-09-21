
class Book(object):

    """ Books class """

    def __init__(self, title, author_sur, author_first, pub_year, user_name, user_id, av_status):
        self.title = title
        self.author_sur = author_sur
        self.author_first = author_first
        self.pub_year = pub_year
        self.user_name = user_name
        self.user_id = user_id
        self.av_status = av_status


    def vacancy_status(self, status):
        """ This method shows name of user that borrowed book"""
        self.user_name = (status.surname, status.first_name)
        self.user_id = status
        return self.user_name

    def av_status_available(self):
        self.user_name = (None,None)
        self.av_status = 'Available'
        return self.user_id

    def av_status_not_available(self):
        self.av_status = 'Not Available'









