#this is for my temp practice

from flask import Flask, redirect, render_template, request, current_app
app = Flask(__name__)
@app.route('/')
def cookie():
    return render_template('cookie.html')


@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user_id = request.form['name']
        redirect_to_welcome = redirect('/welcome')
        response = current_app.make_response(redirect_to_welcome)
        response.set_cookie('user_id', user_id)
        return response
    else:
        return "hehehehehe"

@app.route('/welcome')
def welcome():
    user_id = request.cookies.get('user_id')
    return '<h1>welcome '+user_id+'</h1>'

if __name__ == ('__main__'):
    app.run(debug=True)