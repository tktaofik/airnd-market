from aiohttp import web
from .service import JobService

routes = web.RouteTableDef()

job_service = JobService()


@routes.post('/api/job')
async def post_handler(request: web.Request):
    try:
        job = await job_service.create_job(request)
        return web.json_response(data=job, status=200)
    except Exception as err:
        print(err)
        # return Error.handle(err)
