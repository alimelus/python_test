from datetime import datetime
from flask import Flask, render_template
app = Flask( __name__ )
def hello_world():
    return render_template('index.html', date=datetime.now())
def alive():
    return "yes"
if __name__  == '__main__':
    app.run()
