import sqlite3

from flask import Flask, request

from controllers import user

app = Flask(__name__)

app.register_blueprint(user.user)

print(__name__)


def get_connection():
    conn = sqlite3.connect('/static/db/my.db')
    return conn


@app.route('/', methods=['POST', 'GET'])
def index():
    # conn = get_connection()
    # conn.execute()
    # conn.commit()
    # rows = conn.execute()
    # for r in rows:
    #     r[0]
    if request.method == 'POST':
        if "name" in request.json:
            return "index {}".format(request.json['name'])
        else:
            return "oopps name not specified", 400
    else:
        return "index get"

@app.route('/', methods=['PUT', 'DELETE'])
def index_put():
    print(a)
    return "index"


if __name__ == '__main__':
    app.run(debug=True)
