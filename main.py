from flask import Flask
from flask import request
import pyrebase

app = Flask(__name__)

config = {
  "apiKey": "AIzaSyBXZpwPptJjUJddDl6Q0DpG_3k7mGDdHk8",
  "authDomain": "my-first-project-fea9c.firebaseapp.com",
  "databaseURL": "https://my-first-project-fea9c.firebaseio.com/",
  "storageBucket": "my-first-project-fea9c.appspot.com"
}

firebase = pyrebase.initialize_app(config)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/createuser')
def create_user():
    username = request.headers.get('email')
    password = request.headers.get('password')
    auth = firebase.auth()
    auth.create_user_with_email_and_password(username, password)

@app.route('/login')
def login():
    username = request.headers.get('email')
    password = request.headers.get('password')
    auth = firebase.auth()
    auth.sign_in_with_email_and_password(username, password)