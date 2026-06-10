from flask import Flask

app = Flask(__name__)

@app.route('/python')
def home():
    return '''
    <h1>AletCloud QA - Python Test</h1>
    <p>Framework: Python / Flask</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
