"""
This script runs the FlaskWebProject application using a development server.
"""

from FlaskWebProject import app
import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Change 5000 to your preferred port


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
