from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def calculator():
    # Get numbers from the URL, e.g., /?a=10&b=5
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    op = request.args.get('op', type=str) # add, sub, mul, div

    if a is None or b is None:
        return "<h1>Cloud Calculator</h1><p>Usage: Add ?a=10&b=5&op=add to the URL</p>"

    if op == 'add': result = a + b
    elif op == 'sub': result = a - b
    elif op == 'mul': result = a * b
    elif op == 'div': result = a / b if b != 0 else "Error: Div by Zero"
    else: result = "Invalid Operation"

    return f"<h1>Result: {result}</h1>"

if __name__ == "__main__":
    # Azure Container Apps needs 0.0.0.0 to work!
    app.run(host='0.0.0.0', port=8000)
