
import os
import sys
from marshmallow import ValidationError
import json
from flask import request, Response, jsonify
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.device import deviceConfigModel
from services.device import getDeviceInfoService
from repositories.db import addDevice


def deviceConfigController(data):
    schema = deviceConfigModel()
    try:
        validatedData = schema.load(data)
        result = addDevice(validatedData['device_sid'], 
                            validatedData['hostname'], 
                            validatedData['company_id'], 
                            validatedData['ip'], 
                            validatedData['mac'])
        
        return validatedData, result

    except ValidationError as err:
        print("Validation error:", err)
        return False, err
    
def getDeviceInfo():
    try:
        data = request.get_json()
        deviceInfo = getDeviceInfoService(data['device_id'])
        deviceInfoJson = json.dumps(deviceInfo, indent=4)
        
        return Response(deviceInfoJson, mimetype='application/json' ), 200
    
    except Exception as e:
        print("Error getting device info:", str(e))
        errorResponse = {"status":"error", "message":str(e)}
        errorResponseJson = json.dumps(errorResponse, indent=4)

        return Response(errorResponseJson, mimetype='application/json'), 500


