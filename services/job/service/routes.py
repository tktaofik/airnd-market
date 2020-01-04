import json

from pydash import pick
from aiohttp import web
from .service import JobService
from .utils import json_serial, get_create_job_properties

routes = web.RouteTableDef()


@routes.post('/api/job')
async def post_handler(request):
    job_properties = get_create_job_properties()

    data = json.loads(await request.text())
    data = pick(data, job_properties)

    job = await JobService.create_job(data)
    job_json = json.dumps(job, default=json_serial)

    return web.json_response(body=job_json, status=200)
