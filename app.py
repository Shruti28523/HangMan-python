from flask import Flask, render_template, jsonify
from game.words import load_words
import webbrowser
from threading import Timer

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-word/<category>")
def get_word(category):

    word = load_words(category)

    return jsonify({
        "word": word
    })


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)