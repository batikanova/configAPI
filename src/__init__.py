
from flask import Flask
from flask_socketio import SocketIO
from .events import registerSockets 
from .routes import registerRoutes


def createApp():

    app = Flask(__name__)
    socketio = SocketIO(app, cors_allowed_origins="*")


    # Register routes from the routes module
    registerRoutes(app)
    registerSockets(socketio)

    return socketio, app