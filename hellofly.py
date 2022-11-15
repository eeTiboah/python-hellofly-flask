from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name="Emmanuel"):
    return render_template('hello.html', name=name)

