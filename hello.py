# this is my first flask app
from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    return "Hello world {}".format(name)
# there is also another way of assigning url
# app.add_url_rule('/', '', hello_world)

@app.route('/date/')
def date_time():
    return str(datetime.now())

if __name__ == '__main__':
    app.run(debug=True)
    