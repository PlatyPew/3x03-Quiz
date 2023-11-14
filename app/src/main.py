#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

import re
import secrets

INDEX_PAGE = "index.html"
SANITISED_PATTERN = re.compile(r"^[a-zA-Z0-9 ]+$")

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_bytes(64)

csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template(INDEX_PAGE)


@app.route('/submit', methods=["POST"])
def submit():
    try:
        search = request.form["search"]

        if not _check_sanitise(search):
            return render_template(INDEX_PAGE, result="Nice try"), 400

        return render_template(INDEX_PAGE, result=f"Showing results for: {search}"), 200
    except Exception as e:
        return str(e), 500


# Sanitise for XSS and SQLi
def _check_sanitise(password: str) -> bool:
    if SANITISED_PATTERN.match(password):
        return True

    return False


if __name__ == '__main__':
    app.run(debug=True)
