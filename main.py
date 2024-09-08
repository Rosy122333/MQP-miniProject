#!/bin/python
from flask import Flask, render_template, request, render_template_string
# import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") ##would need a template folder and then need index.html in there and then this works

@app.route('/submit', methods=['POST'])
def submit():
    textbox_value = request.form.get('textbox')
    return f'You submitted: {textbox_value}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)