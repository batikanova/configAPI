ADD_DEVICE_QUERY = """ INSERT INTO devices (device_id, hostname, company_id, device_ip, mac_address) VALUES (%s, %s, %s, %s, %s) """
GET_DEVICE_BY_ID_QUERY = """ SELECT * FROM devices WHERE device_id = %s """
