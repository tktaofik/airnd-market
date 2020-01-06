import json

from pydash import pick
from aiohttp import web
from .service import JobService
from .utils import json_serialize, get_create_job_properties

routes = web.RouteTableDef()


@routes.post('/api/job')
async def post_handler(request: web.Request):
    job_properties = get_create_job_properties()

    data = json.loads(await request.text())
    data = pick(data, job_properties)

    job = await JobService.create_job(data)
    job_json = json.dumps(job, default=json_serialize)

    return web.json_response(body=job_json, status=201)


@routes.get('/api/job/{id}')
async def get_handler(request: web.Request):
    id: int = int(request.match_info['id'])

    job = await JobService.get_job(id)

    if job == None:
        return web.json_response(status=404)

    job_json = json.dumps(job, default=json_serialize)
    return web.json_response(body=job_json, status=200)


@routes.delete('/api/job/{id}')
async def delete_handler(request: web.Request):
    id: int = int(request.match_info['id'])
    await JobService.delete_job(id)
    return web.json_response(status=204)
