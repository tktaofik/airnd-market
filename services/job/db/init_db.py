import os
import enum
from datetime import datetime
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, Enum, String, Date, create_engine
)

user = os.getenv("POSTGRES_USER", "root")
password = os.getenv("POSTGRES_PASSWORD", "password")
host = os.getenv("POSTGRES_HOST", "localhost")
port = os.getenv("POSTGRES_PORT", 5432)

meta = MetaData()


class Status(enum.Enum):
    new = "new"
    inProgress = "inProgress"
    cancelled = "cancelled"
    done = "done"


job = Table(
    'job', meta,
    # sqlalchemy Data types https://www.oreilly.com/library/view/essential-sqlalchemy/9780596516147/ch04.html
    Column('id', Integer, primary_key=True),
    Column('userId', String),
    Column('riderId', String),
    Column('title', String),
    Column('status', Enum(Status), default=Status.new),
    Column('address', String),
    Column('description', String),
    Column('createdAt', Date, default=datetime.now()),
    Column('updatedAt', Date, default=datetime.now())
)


def init_database(db_url):
    db = create_engine(db_url)
    if not database_exists(db.url):
        create_database(db.url)
    return db


def create_tables(db):
    meta = MetaData()
    meta.create_all(bind=db, tables=[job])


def add_sample_data(db):
    conn = db.connect()
    conn.execute(job.insert(), [
        {'userId': 'sdfw23dwed23d'}
    ])
    conn.close()


if __name__ == '__main__':
    db_url = f"postgresql://{user}:{password}@{host}:{port}/job-service"
    db = init_database(db_url)
    create_tables(db)
    # add_sample_data(db)
    print(f"Database created: {db_url}")
