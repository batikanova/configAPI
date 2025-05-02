import socketio

# SocketIO client'ı başlat
sio = socketio.Client()

# Bağlantı kurulduğunda çalışacak fonksiyon
@sio.event
def connect():
    print("Successfully connected to the server.")

# Bağlantı kesildiğinde çalışacak fonksiyon
@sio.event
def disconnect():
    print("Disconnected from the server.")

@sio.event
def device_config_response(data):
    print("Received device config response:", data)
    
@sio.event
def client_list(data):
    print("Received client_list:", data)
    
# Sunucuya bağlan
def connect_to_server():
    # Sunucunun adresini belirtiyoruz
    server_url = "http://localhost:5000"  # Sunucunun adresi
    sio.connect(server_url)

if __name__ == "__main__":
    connect_to_server()
    
    # Eventleri dinlemeye başlamak için infinite loop
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Client has been stopped.")
        sio.disconnect()  # Bağlantıyı kes
