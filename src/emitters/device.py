from src.extensions.socketio import socketio 

def deviceConfigSend(data, sid):
    socketio.emit('config_command', data, room=sid)

def configResponse():
    socketio.emit('config_response', "Successfully registered to the server.")