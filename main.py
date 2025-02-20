from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, BU 5555'

if __name__ == '__main__':
    app.run(debug=True)
