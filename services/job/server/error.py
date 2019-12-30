from pydash import has
from aiohttp import web


class Error:
    def __init__(self, message="internal server error", code=500):
        self.message = message
        self.status = code

    @staticmethod
    def handle(err: Exception) -> web.Response:
        """
        handles exceptions in service

        @param err: (Exception) error to handle
        @returns: json respone
        """
        err_ctx = err.args[0]
        if pydash.has(err_ctx, 'code') is True:
            return web.json_response(err_ctx, status=err_ctx['status_code'])
        else:
            return web.json_response({
                'message': message,
                'code': 500
            }, status=500)
