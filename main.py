from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "hello world!"}

app.run(debug=True)