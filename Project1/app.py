from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def testing():
    return render_template("home.html")

@app.route('/test2')
def testing2():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)