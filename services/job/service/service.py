import json
from aiohttp import web
# from db.tables import job


class JobService:

    async def create_job(self, request):
        body = json.loads(await request.text())
        return body
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
