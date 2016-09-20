# Library Import

from flask import Flask, redirect, url_for, request, render_template


# Script Import
import control
#import book
#import shelf
#import user
#import userdatabase

app = Flask(__name__)

""" Render Index """


@app.route('/')
def index():
    return render_template('index.html')

""" Render User Login"""


@app.route('/user_login')
def user_login():
    return render_template('user_login.html')

""" Render System Login """


@app.route('/system_login')
def system_login():
    return render_template('system_login.html')

""" Render Main System"""


@app.route('/main_system')
def main_system():
    return render_template('main_system.html')

""" Render Add Book"""

@app.route('/book_form')
def book_form():
    return render_template('book_form.html')


@app.route('/user_form')
def user_form():
    return render_template('user_form.html')


@app.route('/search_book')
def search_book():
    return render_template('search_book_form.html')


@app.route('/search_user')
def search_user():
    return render_template('search_user_form.html')


@app.route('/search_book_user_side')
def search_book_user_side():
    return render_template('search_book_form_user_side.html')


""" Main Menu Functions """


@app.route('/menu_main', methods=['POST'])
def menu_main():

    if request.form['submit'] == 'Add Book':
        return redirect(url_for('book_form'))

    elif request.form['submit'] == 'Add User':
        return redirect(url_for('user_form'))

    elif request.form['submit'] == 'Search User':
        return redirect(url_for('search_user'))

    elif request.form['submit'] == 'Search Book':
        return redirect(url_for('search_book'))

    elif request.form['submit'] == 'return':
        return redirect(url_for('index'))


""" Login Functions """


@app.route('/login', methods=['POST'])
def login():

    if request.form['login'] == 'User Login':
        return redirect(url_for('user_login'))

    elif request.form['login'] == 'System Login':
        return redirect(url_for('system_login'))


@app.route('/user_validate', methods=['POST'])
def user_validate():

    if request.form['login'] == 'Per' and request.form['pass'] == '1234':
        # call control.login_function
        return redirect(url_for('search_book_user_side'))

    else:

        return render_template('user_login.html')


@app.route('/system_validate', methods=['POST'])
def system_validate():

    if request.form['login'] == 'Per' and request.form['pass'] == '1234':
        return redirect(url_for('main_system'))

    else:

        return render_template('system_login.html')


""" Add Book Function """

@app.route('/book_form_add', methods=['POST'])
def book_form_add():
    title = request.form['title']
    author_sur = request.form['author_sur']
    author_first = request.form['author_first']
    pub_year = request.form['pub_year']

    m = control.control.add_book_function(title,author_sur,author_first,pub_year)

    print m.title, m.author_sur, m.author_first, m.pub_year, m.user_name

    return redirect(url_for('book_template', title=m.title,
                            author_sur=m.author_sur,
                            author_first=author_first,
                            pub_year=m.pub_year,
                            av_status=None,
                            status=m.user_name))

""" Button for Add Book Function """


@app.route('/book_form_return', methods=['POST'])
def book_form_return():

    if request.form['return'] == 'return':
        return redirect(url_for('main_system'))


""" Add User Function """


@app.route('/user_form_add', methods=['POST'])
def user_form_add():

    surname = request.form['surname']
    first_name = request.form['first_name']
    date_of_birth = request.form['date_of_birth']

    m = control.control.add_user_function(surname, first_name, date_of_birth)


    print m.surname, m.first_name, m.date_of_birth

    return redirect(url_for('user_template', surname=m.surname,
                           first_name=m.first_name,
                           date_of_birth=m.date_of_birth,
                           borrowed_books=m.borrowed_books ))

""" Button for Add User Function """


@app.route('/user_form_return', methods=['POST'])
def user_form_return():

    if request.form['return'] == 'return':
        return redirect(url_for('main_system'))


""" Book Template Function """


@app.route('/book_template')
def book_template():
    return render_template('book_template.html',
                           title=request.args.get('title'),
                           author_sur=request.args.get('author_sur'),
                           author_first=request.args.get('author_first'),
                           pub_year=request.args.get('pub_year'),
                           av_status=request.args.get('av_status'),
                           status=request.args.get('status'))


""" Button for Book Template """


@app.route('/book_template_return', methods=['POST'])
def book_template_return():

    if request.form['button'] == 'return':
        return redirect(url_for('book_form'))


""" Book Template Search"""

@app.route('/book_template_search')
def book_template_search():
    return render_template('book_template_search.html',
                           title=request.args.get('title'),
                           author_sur=request.args.get('author_sur'),
                           author_first=request.args.get('author_first'),
                           pub_year=request.args.get('pub_year'),
                           av_status=request.args.get('av_status'),
                           status=request.args.get('status'))

""" Button for Book Template Search """


@app.route('/book_template_search_return', methods=['POST'])
def book_template_search_return():

    if request.form['button'] == 'return':
        return redirect(url_for('search_book'))


""" Book Template Function User Side """


@app.route('/book_template_user_side')
def book_template_user_side():
    return render_template('book_template_user_side.html',
                           title=request.args.get('title'),
                           author_sur=request.args.get('author_sur'),
                           author_first=request.args.get('author_first'),
                           pub_year=request.args.get('pub_year'),
                           av_status=request.args.get('av_status'),
                           status=request.args.get('status'))


""" Button for Book Template User Side """


@app.route('/book_template_return_user_side', methods=['POST'])
def book_template_return_user_side():

    if request.form['button'] == 'return':
        return redirect(url_for('search_book_user_side'))

    elif request.form['button'] == 'Borrow Book':
        pass


""" User Template Function """


@app.route('/user_template')
def user_template():
    return render_template('user_template.html',
                           surname=request.args.get('surname'),
                           first_name=request.args.get('first_name'),
                           date_of_birth=request.args.get('date_of_birth'),
                           borrowed_books=request.args.get('borrowed_books'))


""" Button for User Template """

@app.route('/user_template_return', methods=['POST'])
def user_template_return():

    if request.form['button'] == 'return':
        return redirect(url_for('user_form'))


""" User Template Search Function """


@app.route('/user_template_search')
def user_template_search():
    return render_template('user_template_search.html',
                           surname=request.args.get('surname'),
                           first_name=request.args.get('first_name'),
                           date_of_birth=request.args.get('date_of_birth'),
                           borrowed_books=request.args.get('borrowed_books'))


""" Button for User Search Template """

@app.route('/user_template_search_return', methods=['POST'])
def user_template_search_return():

    if request.form['button'] == 'return':
        return redirect(url_for('search_user'))


""" Search functions """


""" Book Search function """

@app.route('/book_search', methods=['POST'])
def book_search():

    field = request.form['field']

    if request.form['search'] == 'Search by Title':

        found_object_a = control.control.search_book_function_a(field)

        if found_object_a is False:
            return redirect(url_for('search_book'))

        else:

            return redirect(url_for('book_template_search', title=found_object_a.title,
                                    author_sur=found_object_a.author_sur,
                                    author_first=found_object_a.author_first,
                                    pub_year=found_object_a.pub_year,
                                    av_status=None,
                                    status=found_object_a.user_name))

    elif request.form['search'] == 'Search by Surname':
        found_object_b = control.control.search_book_function_b(field)

        if found_object_b is False:
            return redirect(url_for('search_book'))

        else:

            return redirect(url_for('book_template_search', title=found_object_b.title,
                                    author_sur=found_object_b.author_sur,
                                    author_first=found_object_b.author_first,
                                    pub_year=found_object_b.pub_year,
                                    av_status=None,
                                    status=found_object_b.user_name))

    elif request.form['search'] == 'Search by First Name':
        found_object_c = control.control.search_book_function_c(field)

        if found_object_c is False:
            return redirect(url_for('search_book'))

        else:

            return redirect(url_for('book_template_search', title=found_object_c.title,
                                    author_sur=found_object_c.author_sur,
                                    author_first=found_object_c.author_first,
                                    pub_year=found_object_c.pub_year,
                                    av_status=None,
                                    status=found_object_c.user_name))

""" Button for Book Search Function """


@app.route('/book_search_return', methods=['POST'])
def book_search_return():

    if request.form['return'] == 'return':
        return redirect(url_for('main_system'))


""" Book Search function User Side """


@app.route('/book_search_user_side', methods=['POST'])
def book_search_user_side():

    field = request.form['field']

    if request.form['search'] == 'Search by Title':

        found_object_a = control.control.search_book_function_a(field)

        if found_object_a is False:
            return redirect(url_for('search_book_user_side'))

        else:

            return redirect(url_for('book_template_user_side', title=found_object_a.title,
                                    author_sur=found_object_a.author_sur,
                                    author_first=found_object_a.author_first,
                                    pub_year=found_object_a.pub_year,
                                    av_status=None,
                                    status=found_object_a.user_name))

    elif request.form['search'] == 'Search by Surname':
        found_object_b = control.control.search_book_function_b(field)

        if found_object_b is False:
            return redirect(url_for('search_book_user_side'))

        else:

            return redirect(url_for('book_template_user_side', title=found_object_b.title,
                                    author_sur=found_object_b.author_sur,
                                    author_first=found_object_b.author_first,
                                    pub_year=found_object_b.pub_year,
                                    av_status=None,
                                    status=found_object_b.user_name))

    elif request.form['search'] == 'Search by First Name':
        found_object_c = control.control.search_book_function_c(field)

        if found_object_c is False:
            return redirect(url_for('search_book_user_side'))

        else:

            return redirect(url_for('book_template_user_side', title=found_object_c.title,
                                    author_sur=found_object_c.author_sur,
                                    author_first=found_object_c.author_first,
                                    pub_year=found_object_c.pub_year,
                                    av_status=None,
                                    status=found_object_c.user_name))

""" Buttons for Book Search Function User Side """


@app.route('/book_search_return_user_side', methods=['POST'])
def book_search_return_user_side():

    if request.form['return'] == 'return':
        return redirect(url_for('index'))


""" User Search Function """


@app.route('/user_search', methods=['POST'])
def user_search():

    field = request.form['field']

    if request.form['search'] == 'Search by Surname':

        found_object_a = control.control.search_user_function_a(field)

        if found_object_a is False:
            return redirect(url_for('search_user'))

        else:

            return redirect(url_for('user_template_search', surname=found_object_a.surname,
                                    first_name=found_object_a.first_name,
                                    date_of_birth=found_object_a.date_of_birth,
                                    borrowed_books=found_object_a.borrowed_books))

    elif request.form['search'] == 'Search by First Name':
        found_object_b = control.control.search_user_function_b(field)

        if found_object_b is False:
            return redirect(url_for('search_user'))

        else:
            return redirect(url_for('user_template_search', surname=found_object_b.surname,
                                    first_name=found_object_b.first_name,
                                    date_of_birth=found_object_b.date_of_birth,
                                    borrowed_books=found_object_b.borrowed_books))

""" Button for User Search Function """


@app.route('/user_search_return', methods=['POST'])
def user_search_return():

    if request.form['return'] == 'return':
        return redirect(url_for('main_system'))

""" Run function """

if __name__ == '__main__':
    app.run(debug = True)