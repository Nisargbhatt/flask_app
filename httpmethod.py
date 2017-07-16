# this is my first login api

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name = user))
    else:
       user = request.args.get('name')
       return redirect(url_for('success',name = user))

@app.route('/sucess/<name>') 
def success(name):
    return "Welcome {}".format(name)

if __name__ == '__main__':
    app.run(debug=True)