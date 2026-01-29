from flask import Flask
import os

application = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>The Door is Open!</h1>"

if __name__ == "__main__":
    # 0.0.0.0 tells Python to listen to Azure's requests
    # port 8000 matches the 'target-port' we set in Azure
    app.run(host='0.0.0.0', port=8000)
