import os
import sys
import json
from repositories.db import getDeviceInfoFromDatabase

def getDeviceInfoService(deviceId):
    
    deviceInfo = getDeviceInfoFromDatabase(deviceId)
    return deviceInfo
