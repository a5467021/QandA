"""
This script runs the reflector_backend application using a development server.
"""

from os import environ
from reflector_backend import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '3001'))
    except ValueError:
        PORT = 3001
    app.run(HOST, PORT)
