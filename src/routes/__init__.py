from .device import device

def registerRoutes(app):
    app.register_blueprint(device, url_prefix='/device')
