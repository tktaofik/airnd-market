from aiohttp import web


class UserError(Exception):
    def __init__(self, message="User service error", status=500):
        self.message = str(message)
        self.status = status
