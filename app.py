from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Please enter a song.'

@app.route('/sample')
def sample():
    return 'Now sampling...'