from model import *
from ariadne import convert_kwargs_to_snake_case
import time
from api.store import NewData,queues

async def createSensors_resolver(obj, info, sensor_id, _field, _value):
    try:
        write_api = db.write_api()
        p = Point("airSensors").tag("sensor_id", sensor_id).field(_field, _value)
        write_api.write(bucket = bucket, org = org, record = p, time_precision='ms', protocol = 'json')
        payload = {
            "success": True,
            "post": "Sensor ID {} created with field {} and value {}".format(sensor_id, _field,_value)
        }
        result = {
                "_measurement": "airSensors",
                "sensor_id": sensor_id,
                "_field": _field,
                "_value": _value
        }
        NewData.append(result)
        for queue in queues:
            await queue.put(result)
    except ValueError:
        payload = {
            "success": False,
            "errors": ValueError
        }
    return payload