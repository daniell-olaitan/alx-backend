#!/usr/bin/env python3
"""
Flask app to learn i18n
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration file for the application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """
    Get the locale of the user
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Display the home page
    """
    return render_template('1-index.html')


app.config.from_object(Config)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
