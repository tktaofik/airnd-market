import json

from aiohttp import web
from .error import JobError


@web.middleware
async def error_middleware(request, handler):
    body = 'Internal server error'
    status = 500

    # TODO:Clean headers in response

    try:
        response = await handler(request)
        return response
    except JobError as err:
        body = json.dumps(err.message)
        status = err.status
        return web.json_response(body=body, status=status)
    except Exception as err:
        print(f"### Internal error: {err}")
        return web.json_response(body=body, status=status)
