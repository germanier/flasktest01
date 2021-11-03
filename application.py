from flask import Flask
application = Flask(__name__)

@application.route('/')

def index():
    title = "Rick Astley - Never Gonna Give You Up"
    return title
    a = "never gonna let you down"

@application.route('/api/testimonials')
def testimonials():
    return{'testimonials': ['great', 'sublime', 'delicious']}
