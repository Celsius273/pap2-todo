from flask import Flask
from flask import request
from flask import jsonify
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

@app.route('/createlist')
def create_list():
    owner = request.headers.get('owner')
    list_name = request.headers.get('name')

    db = firebase.database()

    list_data = {
        'owner': owner,
        'name': list_name
    }

    resp = db.child("lists").push(list_data)
    return resp["name"]

@app.route('/list')
def get_list():
    list_id = request.headers.get('listID')

    db = firebase.database()

    data = db.child('lists').child(list_id).get()
    return jsonify(data.val())