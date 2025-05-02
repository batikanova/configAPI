from .device import registerConfigHandlers

def registerSockets(socketio):
    registerConfigHandlers(socketio)