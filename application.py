from flask import Flask
application = Flask(__name__)

@application.route('/')

def helloWorld():
    return 'never gonna give you up'