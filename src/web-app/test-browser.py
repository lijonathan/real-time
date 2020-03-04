from flask import Flask

# Display in browser
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run()
