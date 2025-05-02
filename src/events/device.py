
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.device import deviceConfigController
from flask import request
from src.emitters import configResponse, deviceConfigSend, sendConnectedClients


connectedClients = {}

def registerConfigHandlers(socketio):
    
    @socketio.event
    def device_config(data):
        if data['device_sid'] in connectedClients:
            response, result = deviceConfigController(data)
            print("Response from deviceConfigController:", response)
            if response == False:
                configResponse({'message': 'Device gave an error'})
            else:
                deviceConfigSend(response, data['device_sid'])
        else:
            configResponse({'message': 'Device not connected'})

    
    @socketio.event
    def register(data):
        deviceSid = request.sid
        connectedClients[deviceSid] = data['deviceInfo']
        print(connectedClients)
        sendConnectedClients(connectedClients)

    
    @socketio.event
    def disconnect():
        deviceSid = request.sid
        print(f"Bağlantı kesildi: {deviceSid}")
        if deviceSid in connectedClients:
            print(f"Bağlantı koptu: {connectedClients[deviceSid]}")
            connectedClients.pop(deviceSid)

        sendConnectedClients(connectedClients)
    
    @socketio.event
    def connect():
        deviceSid = request.sid
        print(f"Bağlantı kuruldu: {deviceSid}")
