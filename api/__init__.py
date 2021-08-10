from flask import Flask
from flask_cors import CORS
from flask import render_template


app = Flask(__name__)
#app.config.from_object('config')
CORS(app)


@app.route('/')
def hello():
    return render_template("index.html")
    #return 'My First API !!'