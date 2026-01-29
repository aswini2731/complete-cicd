from flask import Flask

application = Flask(__name__)
app = application # This ensures 'app' is available for Gunicorn

@app.route('/')
def home():
    return "<h1>Calculator is Live!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
