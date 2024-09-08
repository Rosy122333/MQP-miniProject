#!/bin/python
from flask import Flask, render_template, request, render_template_string
from langchain_ollama import OllamaLLM
import requests
import json
app = Flask(__name__)
model = OllamaLLM(model="llama3:latest")
message = ""
@app.route('/')
def index():
    return render_template("index.html") ##would need a template folder and then need index.html in there and then this works

@app.route('/submit', methods=['POST'])
def submit():
    textbox_value = request.form.get('textbox')
    message = textbox_value
    result = model.invoke(input=message)
    return f'Ollama returned: {result}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)