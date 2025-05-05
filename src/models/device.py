from marshmallow import Schema, fields, ValidationError, validates # type: ignore
from extensions.db import dbConn, returnConn, closePool # type: ignore

class deviceConfigModel(Schema):
    device_sid = fields.String(required=True)
    configs = fields.Dict(
        keys=fields.String(), 
        values=fields.Dict(
            keys=fields.String(),
            values=fields.Raw()
        ),
        required=True
    )
    
    
    
    




