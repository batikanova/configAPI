
from flask import Flask, Response
from src.extensions.socketio import socketio  # Buradan socketio'yu import ediyoruz
from .events import registerSockets 
from .routes import registerRoutes
import json


def createApp():

    app = Flask(__name__)
    
    @app.route('/')
    def home():
        homeInfo = {
            "status": "success",
            "message": "Welcome to the Flask-SocketIO application!",
            "routes": {
                "/": "Home route",
                "/device": "Device API route",
                "/device/getConfigInfo": "Device info route"
            }
            }
        homeInfo = json.dumps(homeInfo, indent=4)
        return Response(homeInfo, mimetype='application/json'), 200

    socketio.init_app(app)
    
    registerRoutes(app)
    registerSockets(socketio)

    return socketio, app