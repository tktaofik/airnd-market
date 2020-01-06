import json

from aiohttp import web
from . import db
from .error import JobError


class JobService:

    @staticmethod
    async def create_job(data):
        job = await db.create_job(data)
        return job

    def delete_job(self):
        print("delete_job") 

        

    def update_job(self):
        print("update_job")

    def get_job(self):
        print("get_job")

    def find_jobs(self):
        print("find_jobs")
