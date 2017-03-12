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

@app.route('/createlist')
def create_list():
    owner = request.headers.get('owner')
    list_name = request.headers.get('name')

    db = firebase.database()
    new_list_key =  db.generate_key()
    print new_list_key
    list_data = {
        'owner': owner,
        'name': list_name
    }
#{'owner': str(owner),'name': str(list_name)}
    # db.child("lists").push(new_list_key)
    db.child("lists").push(list_data)
    # db.update(list_data)
    # db.child("lists").child(new_list_key).set(list_data)

    return new_list_key
