from marshmallow import Schema, fields, ValidationError, validates # type: ignore
from extensions.db import dbConn, returnConn, closePool # type: ignore

class deviceConfigModel(Schema):
    device_sid = fields.String(required=True)
    hostname = fields.String(required=True)
    ip = fields.String(required=True)
    mac = fields.String(required=True)
    company_id = fields.String(required=True)




