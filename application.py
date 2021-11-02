from flask import Flask
application = Flask(__name__)

@application.route('/')

def helloWorld():
    print("never gonna give you up, ")
    return "never gonna let you down"