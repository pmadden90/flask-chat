import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello there!</h1>"

app.run(os.getenv('IP'), port=int(os.getenv('PORT', '8080')), debug=True)