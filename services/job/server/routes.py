import json
from aiohttp import web
from .service import JobService

routes = web.RouteTableDef()

job_service = JobService()


async def get_handler(request):
    job_service.create_job("efr")
    return web.Response(text="'Hello Aiohttp! ewwe'")


@routes.post('/api/job')
async def post_handler(request: web.Request):
    try:
        body = json.loads(await request.text())
        # await EndpointCacher.create(ctx, DB.get_redis(request), DB.get(request, controller.table))
        # job_service.create_job("efr")
        return web.json_response(data=body, status=200)
    except Exception as err:
        print(err)
        # return Error.handle(err)
    return web.Response(text="'Hello Aiohttp! ewwe'")
