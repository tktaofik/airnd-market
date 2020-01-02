import json
from aiohttp import web

from . import db


class JobService:

    @staticmethod
    async def create_job(request):
        data = json.loads(await request.text())
        try:
            job = await db.create_job(data)
            return job
        except Exception as err:
            print(err)

    def delete_job(self):
        print("delete_job")

    def update_job(self):
        print("update_job")

    def get_job(self):
        print("get_job")

    def find_jobs(self):
        print("find_jobs")
