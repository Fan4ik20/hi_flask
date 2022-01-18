from flask import render_template, request, abort

from app import app

from hello_db.models_manager import UserManager


user_manager = UserManager()


@app.route('/', methods=['GET', 'POST'])
def show_index():
    if request.method == 'POST':
        name = request.form.get('firstName')
        surname = request.form.get('lastName')

        if not name:
            return abort(400)

        already_visited = user_manager.check_user_exists(name, surname)

        if not already_visited:
            user_manager.add_user(name, surname)

        return render_template(
            'pages/welcome_page.html', first_name=name, last_name=surname,
            already_visited=already_visited
        )

    return render_template('pages/welcome_page.html')


@app.route('/users/')
def show_users():
    users = user_manager.get_all_users()

    return render_template('pages/show_users_page.html', users=users)
