<<<<<<< HEAD
import os
from flask import Flask, render_template, request

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template("main.html")
=======
from app import app
>>>>>>> 48f1e81f151f10a4d998c204b3ab59e2493617b1

if __name__ == "__main__":
    app.run(port = 5000, debug = True)