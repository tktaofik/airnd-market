import json

from pydash import pick
from aiohttp import web
from .service import JobService
from .utils import json_serial
from .db import job as job_table

routes = web.RouteTableDef()


@routes.post('/api/job')
async def post_handler(request):
    try:
        data = json.loads(await request.text())
        data = pick(data, job_table.columns.keys())
        job = await JobService.create_job(data)
        job_json = json.dumps(job, default=json_serial)
        return web.json_response(body=job_json, status=200)
    except Exception as err:
        print(err)
