from aiohttp import web
from .service import JobService

routes = web.RouteTableDef()

job_service = JobService()


@routes.get('/api/job')
async def handle(request):
    job_service.create_job("efr")
    return web.Response(text="'Hello Aiohttp! ewwe'")


@routes.post('/api/job')
async def handle(request):
    job_service.create_job("efr")
    return web.Response(text="'Hello Aiohttp! ewwe'")
