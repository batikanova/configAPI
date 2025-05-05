import sys
import os
from flask import Blueprint, request, jsonify, Response
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.device import getDeviceInfo
import json
device = Blueprint('device', __name__)

@device.route('/', methods=['GET'])
def getDeviceRoutes():
    routesInfo = {
        "routes": [
            {
                "path": "/device/getConfigInfo",
                "method": "GET",
                "parameters":"{'device_id':'device_id'}",
                "description": "Get device configuration information"}],
        "socketEvents": [
            {
                "event": "device_config",
                "description": "Socket event for device configuration",
                "parameters":"{'device_sid':device_sid, 'configs':configs}",
                "responseEvent": "device_config_response"
            },
            {
                "event": "register",
                "description": "Socket event for registering device",
                "parameters":"{'deviceInfo':device_info}",
                "responseEvent": "client_list" },
            {
                "event": "disconnect",
                "description": "Socket event for device disconnection",
                "responseEvent": "client_list"}]
        }
    routesInfoJson = json.dumps(routesInfo, indent=4)
    return Response(routesInfoJson, mimetype='application/json'), 200
            
    
@device.route('/getConfigInfo', methods=['GET'])
def getInfo():
    return getDeviceInfo()
