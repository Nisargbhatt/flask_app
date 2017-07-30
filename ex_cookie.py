# example for setting cookie

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def ex_cookie():
    return render_template('cookie.html')


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method = 'POST':
        name = request.form['nm']
        rasp = make_response(render_template('readcookie.html'))
        rasp = set_cookie('userID', user)

    return rasp    

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'