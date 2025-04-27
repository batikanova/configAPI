from .device_socketio import registerConfigHandlers

def registerSockets(socketio):
    registerConfigHandlers(socketio)