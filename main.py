"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, ssl_context='adhoc')
"""
This script runs the FlaskWebProject application using a development server.
"""

''''import os
from FlaskWebProject import app

if __name__ == '__main__':
    # Use Azure's assigned PORT, default to 80 if not set
    HOST = '0.0.0.0'
    try:
        PORT = int(os.environ.get('PORT', 80))
    except ValueError:
        PORT = 80

    # Run the Flask app
    app.run(host=HOST, port=PORT)''''
