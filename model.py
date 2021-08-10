from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "uIqSlzGvQ7lRMWlGpq_5H180p2qx6dJTEW8vL7MppUBf4RUZoEhgSITb8OdCIO0NDUcCYZ1Oil5JzGegwecRSw=="
org = "usmangovedi1@gmail.com"
bucket = "usmangovedi1\'s Bucket"
db = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token)

def to_dict():
    query = f'from(bucket: "usmangovedi1\'s Bucket")\
    |> range(start: -30d)\
    |> filter(fn: (r) => r["_measurement"] == "airSensors")'
    result = db.query_api().query(query, org = org)
    results=[]
    for table in result:
        for record in table.records:
            results.append({
                "_measurement": record['_measurement'],
                "_time": record['_time'],
                "_start":record['_start'],
                "_stop": record['_stop'],
                "sensor_id": record['sensor_id'],
                "_field": record.get_field(),
                "_value": record.get_value()
            })
    return results


def By_sensor_id(sensor_id):
    query = f'from(bucket: "usmangovedi1\'s Bucket")\
    |> range(start: -30d)\
    |> filter(fn: (r) => r["_measurement"] == "airSensors") \
    |> filter(fn: (r) => r["sensor_id"] == "{sensor_id}")'
    result = db.query_api().query(query, org = org)
    results=[]
    for table in result:
        for record in table.records:
            results.append({
                "_measurement": record['_measurement'],
                "_time": record['_time'],
                "_start":record['_start'],
                "_stop": record['_stop'],
                "sensor_id": record['sensor_id'],
                "_field": record.get_field(),
                "_value": record.get_value()
            })
    return results