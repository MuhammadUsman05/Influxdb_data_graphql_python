from model import *
from ariadne import convert_kwargs_to_snake_case

def listSensors_resolver(obj, info):
    try:
        airsensors = [airsensor for airsensor in to_dict()]
        payload = {
            "success": True,
            "post": airsensors
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def bySensorsId_resolver(obj, info, sensor_id):
    try:
        airsensors = [airsensor for airsensor in By_sensor_id(sensor_id)]
        payload = {
            "success": True,
            "post": airsensors
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Post item matching {sensor_id} not found"]
        }
    return payload