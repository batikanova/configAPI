
import os
import sys
from marshmallow import ValidationError
import json
from flask import request, Response, jsonify
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.device import DeviceConfigModel
from services.device_service import deviceConfigService, getDeviceInfoService


def deviceConfigController(data):
    schema = DeviceConfigModel()
    try:
        validatedData = schema.load(data)
        response = deviceConfigService(validatedData)
        return response

    except ValidationError as err:
        print("Validation error:", err.messages)
        return {"error": "Invalid data"}
    
def getDeviceInfo():
    try:
        deviceInfo = getDeviceInfoService()
        deviceInfo = json.dumps(deviceInfo, indent=4)
        
        return Response(deviceInfo, mimetype='application/json' ), 200
    
    except Exception as e:
        print("Error getting device info:", str(e))
        errorResponse = {"status":"error", "message":str(e)}
        errorResponse = json.dumps(errorResponse, indent=4)

        return Response(errorResponse, mimetype='application/json'), 500


