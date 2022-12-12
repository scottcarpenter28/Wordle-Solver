from flask import Flask, render_template, url_for
from os import getenv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    host = getenv("HOST", "0.0.0.0")
    port = int(getenv("PORT", 5000))
    print(f"Starting server at {host}:{port}")

    app.run(
        host="0.0.0.0",
        port=5000,
    )
    url_for('static', filename='css/style.css')
