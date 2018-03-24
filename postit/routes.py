from postit.app import app, postit_pages
from flask import render_template

@app.route("/")
def hello():
    return render_template("index.html", pages=postit_pages.postitpages[0].name)
