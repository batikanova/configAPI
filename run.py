from src import createApp


socketio, app = createApp()

if __name__ == "__main__":
    print("Starting server...")
    socketio.run(app, host="0.0.0.0", port=5000)