import json
from aiohttp import web

from . import db


class JobService:

    @staticmethod
    async def create_job(request):
        async with request.app['db_pool'].acquire() as conn:
            data = json.loads(await request.text())
            try:
                res = await db.create_job(conn, data)
                return res
            except Exception as err:
                print(err)
            # try:
            #     # job = Job()
            #     # for k, v in body.items():
            #     #     setattr(job, k, v)
            #     # session.add(job)
            #     # session.commit()
            #     # session.refresh(job)
            #     # res = session.query(Job).filter(
            #     #     Job.id == job.id).first()

            #     # print(res.tojson())
            #     return body
            # except SQLAlchemyError as e:
            #     print(e)

    def delete_job(self):
        print("delete_job")

    def update_job(self):
        print("update_job")

    def get_job(self):
        print("get_job")

    def find_jobs(self):
        print("find_jobs")
