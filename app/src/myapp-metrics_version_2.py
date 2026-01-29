from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Calculator is Running!</h1><p>To use: add /add/10/20 to the URL</p>"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"<h1>Result: {a + b}</h1>"

if __name__ == "__main__":
    # Port 8000 and 0.0.0.0 are MANDATORY for Azure
    app.run(host='0.0.0.0', port=8000)
