"""
This script runs the FlaskWebProject application using a development server.
"""

from FlaskWebProject import app
import os

if __name__ == "__main__":
    host = "0.0.0.0"                     # Make the app accessible externally
    port = int(os.environ.get("PORT", 8000))  # Use Azure's assigned port or 8000
    app.run(host=host, port=port)

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
