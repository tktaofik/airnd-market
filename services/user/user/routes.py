import json
import logging

from pydash import pick
from aiohttp import web
from .service import UserService
from .utils import json_serialize, get_create_user_properties

routes = web.RouteTableDef()


@routes.get('/ready')
async def ready_handler(request: web.Request):
    return web.json_response(status=200)


@routes.post('/api/user')
async def post_handler(request: web.Request):
    user_properties = get_create_user_properties()

    data = json.loads(await request.text())
    data = pick(data, user_properties)

    user = await UserService.create_user(data)
    user_json = json.dumps(user, default=json_serialize)

    logging.info(f"User created id: {user['id']}")

    return web.json_response(body=user_json, status=201)


# @routes.get('/api/job')
# async def get_jobs_handler(request: web.Request):
#     jobs = await JobService.get_jobs()
#     jobs_json = json.dumps(jobs, default=json_serialize)
#     return web.json_response(body=jobs_json, status=200)


# @routes.get('/api/job/{id}')
# async def get_handler(request: web.Request):
#     id = str(request.match_info['id'])

#     job = await JobService.get_job(id)

#     if job == None:
#         return web.json_response(status=404)

#     job_json = json.dumps(job, default=json_serialize)
#     return web.json_response(body=job_json, status=200)


# @routes.delete('/api/job/{id}')
# async def delete_handler(request: web.Request):
#     id = str(request.match_info['id'])
#     await JobService.delete_job(id)
#     return web.json_response(status=204)
