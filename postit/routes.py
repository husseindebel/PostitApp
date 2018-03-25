from postit.app import app, postit_pages, all_users
from flask import render_template, request , abort , redirect , Response ,url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from postit.model.PostitPage import PostitPage
from postit.model.Users import User

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

@app.route('/add_page', methods=['GET', 'POST'])
def add_page():
    if request.method == 'POST':
        page_name = request.form['name']
        user = User(current_user.name, current_user.password)
        page = PostitPage(page_name, user)
        postit_pages.add_postitpage(page)
        return redirect(url_for('index'))
    return render_template("add_page.html")

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
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_name):
    return all_users.get_user(user_name)


@app.route('/secret', methods=['GET'])
@login_required
def secret():
    return 'This is a secret page. You are logged in as {}'.format(current_user.name)