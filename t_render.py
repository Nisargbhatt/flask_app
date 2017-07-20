# this api will render the template from the folder named tamplate

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/result')
def result():
    dict={'physics':50, 'maths':70, 'history':80}
    return render_template('hello.html',result = dict)

if __name__ == '__main__':
    app.run(debug=True)                                     