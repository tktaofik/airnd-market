import json

from aiohttp import web
from . import db
from .error import JobError


class JobService:

    @staticmethod
    async def create_job(data):
        job = await db.create_job(data)
        return job

    @staticmethod
    async def get_job(id):
        job = await db.get_job(id)
        return job

    @staticmethod
    async def get_jobs():
        jobs = await db.get_jobs()
        return jobs

    @staticmethod
    async def delete_job(id):
        await db.delete_job(id)
