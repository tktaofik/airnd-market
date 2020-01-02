import json

from aiohttp import web
from .service import JobService
from .utils import json_serial

routes = web.RouteTableDef()


@routes.post('/api/job')
async def post_handler(request):
    try:
        data = await JobService.create_job(request)
        data_json = json.dumps(data, default=json_serial)
        return web.json_response(body=data_json, status=200)
    except Exception as err:
        print(err)
