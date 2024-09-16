#!/usr/bin/env python3
"""
Flask app to learn i18n
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    """
    Display the home page
    """
    return render_template('1-index.html')


app.config.from_object(Config)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
