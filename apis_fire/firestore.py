import pyrebase
import os


config = {
 'apiKey': "AIzaSyC7jpBh3CfdpBKUZvpuU7rfH0DvOiEQhDQ",
    'authDomain': "awsapp-6bf1a.firebaseapp.com",
    'databaseURL': "https://awsapp-6bf1a.firebaseio.com",
    'projectId': "awsapp-6bf1a",
    'storageBucket': "awsapp-6bf1a.appspot.com",
  'serviceAccount': str(os.getcwd())+'/awsapi.json'

}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
