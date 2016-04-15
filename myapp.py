from flask import Flask, jsonify, abort, url_for, redirect, render_template, g, request, session, flash

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
