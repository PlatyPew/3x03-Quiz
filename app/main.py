#!/usr/bin/env python3
from flask import Flask, render_template, request

import re
SANITISED_PATTERN = re.compile(r"^[a-zA-Z0-9 ]+$")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=["POST"])
def submit():
    try:
        search = request.form["search"]

        if not _check_sanitise(search):
            return render_template('index.html', result="Nice try"), 400

        return render_template('index.html', result=f"Showing results for: {search}"), 200
    except Exception as e:
        return str(e), 500

# Sanitise for XSS and SQLi
def _check_sanitise(password: str) -> bool:
    if SANITISED_PATTERN.match(password):
        return True

    return False

if __name__ == '__main__':
    app.run(debug=True)
