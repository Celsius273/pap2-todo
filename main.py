from flask import Flask
from flask import request
from firebase import firebase

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/createuser')
def create_user():
    username = request.args.get('username')
    password = request.args.get('password')
