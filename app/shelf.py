""" This is the bookshelf object """


class Shelf(object):
    """ Shelf Class """

    """ List over all books """
    books_list = list()


    """ Functions """

    def add_book(self, books):
            """ This is a complete list of book objects that are added to the library"""
            shelf.books_list.append(books)
            #return shelf.books_list


    def books_title(self):
        """ This function returns a list of all book titles """
        return [i.title for i in shelf.books_list]

    def books_surname(self):
        """ This function returns a list of all author surnames """
        return [i.author_sur for i in shelf.books_list]

    def books_first_name(self):
        """ This function returns a list of all author first names """
        return [i.author_first for i in shelf.books_list]


    """ Other functions """

    def check_book(self):
            """ This method shows whether a book is vacant or not"""
            pass


shelf = Shelf()

