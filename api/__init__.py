from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
#app.config.from_object('config')
CORS(app)


@app.route('/')
def hello():
    return 'My First API !!'