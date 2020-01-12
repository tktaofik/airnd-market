from aiohttp import web
from . import db


class UserService:

    @staticmethod
    async def isReady():
        return True

    @staticmethod
    async def create_user(data):
        user = await db.create_user(data)
        return user
