from marshmallow import Schema, fields, ValidationError, validates # type: ignore


class DeviceConfigModel(Schema):
    
    device_id = fields.String(required=True)
    device_name = fields.String(required=True)
    device_room = fields.String(required=True)
