import sys
import os
from flask import Blueprint, request, jsonify, Response
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.device_controller import getDeviceInfo
import json
device = Blueprint('device', __name__)

@device.route('/', methods=['GET'])
def getDeviceRoutes():
    routesInfo = {
        "routes": [
            {
                "path": "/device/getConfigInfo",
                "method": "GET",
                "description": "Get device configuration information"}],
        "socketEvents": [
            {
                "event": "device_config",
                "description": "Socket event for device configuration",
                "responseEvent": "device_config_response"
            }
        ]
        }
    routesInfo = json.dumps(routesInfo, indent=4)
    return Response(routesInfo, mimetype='application/json'), 200
            
    
@device.route('/getConfigInfo', methods=['GET'])
def getInfo():
    return getDeviceInfo()
