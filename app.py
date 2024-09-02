from flask import Flask, render_template, request
import os
from datetime import datetime
import logging
from logging import FileHandler, Formatter

app = Flask(__name__)

# Configuração de logs
if not app.debug:
    file_handler = FileHandler('logs/error.log')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    app.logger.addHandler(file_handler)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/greet')
def greet():
    user = os.getenv('USER_NAME', 'Guest')
    return f"Hello, {user}! Welcome to your Flask app."

@app.route('/time')
def time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current date and time: {now}"

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


