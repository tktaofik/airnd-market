from pydash import has
from aiohttp import web


class JobError(Exception):
    def __init__(self, message="Job service error", status=500):
        self.message = str(message)
        self.status = status
