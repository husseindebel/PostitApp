from postit.app import app, postit_pages, all_users
from flask import render_template, request , abort , redirect , Response ,url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

login_manager = LoginManager()
login_manager.setup_app(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", pages=postit_pages.postitpages, user=current_user)

@app.route("/p/<page_name>")
@login_required
def page(page_name):
    page = postit_pages.get_page(page_name)
    return render_template("postit_page.html", page=page)

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        current = all_users.get_user(username)

        if current is None or current.password != password:
            return redirect(url_for('index'))
        else: 
            print("logging in...")
            login_user(current)
            current.authenticated = True
            return redirect(url_for('index'))
    else:
        return redirect(url_form('index'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    current_user.authenticated = False
    return Response('<p>Logged out</p>')

@login_manager.user_loader
def load_user(user_name):
    return all_users.get_user(user_name)


@app.route('/secret', methods=['GET'])
@login_required
def secret():
    return 'This is a secret page. You are logged in as {}'.format(current_user.name)