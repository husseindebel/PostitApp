from flask import Flask
from postit.model.Postit import Postit
from postit.model.PostitPage import PostitPage

app = Flask(__name__)

# in memory initialisation
postit_pages = Postit()
page = PostitPage("hussein", "alot of things")
postit_pages.add_postitpage(page)

import postit.routes