"""
The Flask application package.
"""
import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# -----------------------------
# ✅ Logging configuration
# -----------------------------

# 1️⃣ StreamHandler for Azure Log Stream
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Capture INFO, WARNING, ERROR
stream_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(stream_formatter)
app.logger.addHandler(stream_handler)

# 2️⃣ FileHandler for local logs
if not os.path.exists('logs'):
    os.mkdir('logs')  # Create a logs folder if it doesn't exist

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=3)
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
app.logger.addHandler(file_handler)

# Set minimum logging level
app.logger.setLevel(logging.INFO)

# -----------------------------
# Flask extensions
# -----------------------------
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# -----------------------------
# Import views at the end
# -----------------------------
import FlaskWebProject.views
