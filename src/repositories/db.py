from extensions.db import dbConn, returnConn
from models.queries import GET_DEVICE_BY_ID_QUERY, ADD_DEVICE_QUERY

def addDevice(validatedData):
    conn = None
    deviceId = validatedData['device_sid']
    hostname = validatedData['configs']['hostname']
    deviceIp = validatedData['configs']['device_ip']
    macAddress = validatedData['configs']['mac_address']
    companyId = validatedData['configs']['company_id']
    
    try:
        conn = dbConn()
        if conn is None:
            return False

        cursor = conn.cursor()
        cursor.execute(ADD_DEVICE_QUERY, (deviceId, hostname, companyId, deviceIp, macAddress))
        conn.commit()
        return True

    except Exception as e:
        print("Database error while adding device:", str(e))
        return False

    finally:
        if conn:
            returnConn(conn)

def getDeviceInfoFromDatabase(deviceId):
    conn = None
    try:
        conn = dbConn()
        if conn is None:
            return False

        cursor = conn.cursor()
        cursor.execute(GET_DEVICE_BY_ID_QUERY, (deviceId,))
        deviceInfo = cursor.fetchone()

        if deviceInfo:
            return deviceInfo
        else:
            return None

    except Exception as e:
        print("Database error while adding device:", str(e))
        return False

    finally:
        if conn:
            returnConn(conn)
