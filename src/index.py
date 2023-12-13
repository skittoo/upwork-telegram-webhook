from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1> Hello Mety </h1>"

@app.route('/myapp')
def myapp():
    return "<h1> My app is my app </h1>"
