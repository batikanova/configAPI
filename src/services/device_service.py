import os
import sys
import json

def deviceConfigService(data):
    #burada gelen datayı işle env dosyası oluştur veritabanına da kaydet
    basePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    configPath = os.path.join(basePath, 'config', 'device_config.json')
    print(configPath, data)
    with open(configPath, "w") as file:
        json.dump(data, file, indent=4)
    return {"status": "success", "message": "Device configuration processed successfully"}

def getDeviceInfoService():
    basePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    configPath = os.path.join(basePath, 'config', 'device_config.json')
    with open(configPath, "r") as file:
        deviceInfo = json.load(file)
        print(deviceInfo)
        return deviceInfo