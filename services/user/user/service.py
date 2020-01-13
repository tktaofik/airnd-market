from aiohttp import web
from . import db
from .security import hashPassword, verifyPassword


class UserService:

    @staticmethod
    async def isReady():
        return True

    @staticmethod
    async def create_user(data):
        data['password'] = hashPassword(data['password'])
        user = await db.create_user(data)
        return user
