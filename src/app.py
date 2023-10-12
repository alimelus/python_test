from datetime import datetime
from flask import flask, render_template
app = flask(__name__ )
def hello_world():
    return render_template('index.html', date=datetime.now())
def alive():
    return "yes"
if __name__  == '__main__':
    app.run()
