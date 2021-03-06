from sqlalchemy import create_engine, MetaData
from job.db import job
from job.config import get_config

config = get_config()

db_name = config['db_name']
db_port = config['db_port']
db_host = config['db_host']
db_user = config['db_user']
db_password = config['db_password']

engine = create_engine(
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}", isolation_level='AUTOCOMMIT')


def setup_db():
    meta = MetaData()
    meta.drop_all(bind=engine, tables=[job])
    meta.create_all(bind=engine, tables=[job])


def add_sample_data():
    conn = engine.connect()
    conn.execute(job.insert(), [
        {
            "userId": "userId",
            "riderId": "riderId",
            "title": "title",
            "status": "new",
            "pickupAddress": "address",
            "dropoffAddress": "address",
            "description": "description",
        }
    ])
    conn.close()


if __name__ == '__main__':
    setup_db()
    add_sample_data()
    print(f"Database initialized")
