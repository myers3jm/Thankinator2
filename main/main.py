from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test")
def test():
    return "This is a test!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)