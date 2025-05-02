from src.extensions.socketio import socketio 

def sendConnectedClients(connectedClients):
    socketio.emit('client_list', connectedClients)

def configResponse(data):
    socketio.emit('device_config_response', data)