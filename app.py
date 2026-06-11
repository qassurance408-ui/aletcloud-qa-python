import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/python')

@app.route('/python')
def home():
    qa_test = os.environ.get('QA_TEST', 'NOT SET')
    return f'''
    <h1>AletCloud QA - Python Test</h1>
    <p>Framework: Python / Flask</p>
    <p>QA_TEST env var = <strong>{qa_test}</strong></p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
