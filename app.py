# This code is from https://github.com/Umairkhan30/github-actions-practice/edit/main/app.py
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
