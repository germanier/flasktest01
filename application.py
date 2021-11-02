from flask import Flask
application = Flask(__name__)

@application.route('/')

def helloWorld():
    return "never gonna give you up,\n never gonna let you down"