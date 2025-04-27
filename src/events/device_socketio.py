
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.device_controller import deviceConfigController

def registerConfigHandlers(socketio):

    @socketio.on('device_config')
    def handleDeviceConfig(data):
        response = deviceConfigController(data)
        print("Response from deviceConfigController:", response)
        socketio.emit('device_config_response', response)
        
