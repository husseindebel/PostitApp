from postit.app import app, postit_pages, all_users
from flask import render_template, request , abort , redirect , Response ,url_for
# from flask_login import LoginManager, login_user, logout_user, login_required, current_user
# from postit.model.PostitPage import PostitPage
# from postit.model.Users import User
# from postit.model.Posts import Post

@app.route("/")
def hello():
    return render_template("index.html")
