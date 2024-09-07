#!/bin/python
from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") ##would need a template folder and then need index.html in there and then this works

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)