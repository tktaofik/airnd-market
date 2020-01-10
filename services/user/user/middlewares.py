import json
import logging

from aiohttp import web
from .error import UserError


@web.middleware
async def error_middleware(request, handler):
    body = 'Internal server error'
    status = 500
    error = None

    # TODO:Clean headers in response

    try:
        response = await handler(request)
        return response
    except UserError as err:
        error = err
        body = json.dumps(err.message)
        status = err.status
        return web.json_response(body=body, status=status)
    except Exception as err:
        error = err
        print(f"### Internal error: {err}")
        return web.json_response(body=body, status=status)
    finally:
        if error != None:
            logging.error(error)
