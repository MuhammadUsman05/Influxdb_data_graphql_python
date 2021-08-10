import asyncio
from ariadne import convert_kwargs_to_snake_case
from api.store import queues

async def sensorMessages_source(obj,info):
    queue = asyncio.Queue()
    queues.append(queue)
    try:
        while True:
            print('listen')
            message = await queue.get()
            queue.task_done()
            print(message)
            yield message
    except asyncio.CancelledError:
        queues.remove(queue)
        raise

async def sensorMessages_resolver(message, info):
    try:
        payload = {
            "success": True,
            "post": message
    }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
