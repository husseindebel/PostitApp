from flask import Flask 
from postit.model.Postit import Postit
from postit.model.PostitPage import PostitPage
from postit.model.Users import User
from postit.model.UserSystem import UserSystem

app = Flask(__name__)
# in memory initialisation
# this will vary depending on how you receive the input!!
app.secret_key = 'super secret key'
postit_pages = Postit()
all_users = UserSystem()

with open("data.txt", "r") as w:
    for i in range(0, 4):
        (name, password) = w.readline().split()
        user = User(name, password)
        all_users.add_users(user)

    for i in range(0, 3):
        (page_name, name) = w.readline().split()
        current_user = all_users.get_user(name)
        page = PostitPage(page_name, current_user)
        postit_pages.add_postitpage(page)

## print out for sanity sake
for n in postit_pages.postitpages:
    print(n)
print("all users...")
for n in all_users.users:
    print(n)

import postit.routes
