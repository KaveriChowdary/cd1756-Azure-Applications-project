"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# ✅ Configure logging for Azure
# StreamHandler sends logs to Azure Log Stream
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)  # Capture INFO, WARNING, ERROR
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)

# Attach handler to app logger
if not app.logger.handlers:
    app.logger.addHandler(streamHandler)

# Set the minimum logging level for the app
app.logger.setLevel(logging.INFO)

# Flask extensions
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
