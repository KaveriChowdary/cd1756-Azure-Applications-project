"""
This script runs the FlaskWebProject application using a development server.
"""

'''from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, ssl_context='adhoc')'''
"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    # Azure sets the PORT environment variable dynamically
    port = int(environ.get("PORT", 80))  # default to 80 if PORT not set
    app.run(host="0.0.0.0", port=port)   # listen on all network interfaces

