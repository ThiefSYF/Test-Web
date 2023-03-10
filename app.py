from flask import Flask
import os
from flask import render_template
from gevent import pywsgi
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 443), app)
    server.serve_forever()

