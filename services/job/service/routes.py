import json

from aiohttp import web
from .service import JobService

routes = web.RouteTableDef()


@routes.post('/api/job')
async def post_handler(request):
    try:
        data = await JobService.create_job(request)
        return web.json_response(data=data, status=200)
    except Exception as err:
        print(err)
