import enum

import aiopg.sa
import asyncpgsa

from datetime import datetime

from sqlalchemy import (
    create_engine, MetaData, Table, Column, ForeignKey,
    Integer, String, Date, Enum
)


# session should be recreated
# https://stackoverflow.com/questions/12223335/sqlalchemy-creating-vs-reusing-a-session

# python-sqlalchemy
# https://www.pythonsheets.com/notes/python-sqlalchemy.html#insert-create-an-insert-statement

meta = MetaData()


class Status(enum.Enum):
    new = "new"
    inProgress = "inProgress"
    cancelled = "cancelled"
    done = "done"


# sqlalchemy Data types https://www.oreilly.com/library/view/essential-sqlalchemy/9780596516147/ch04.html
job = Table(
    'job', meta,

    Column("id", Integer, primary_key=True),
    Column("userId", String),
    Column("riderId", String),
    Column("title", String),
    Column("status", Enum(Status), default=Status.new),
    Column("pickupAddress", String),
    Column("dropoffAddress", String),
    Column("description", String),
    Column("createdAt", Date, default=datetime.now()),
    Column("updatedAt", Date, default=datetime.now())
)


async def init_db(app):
    config = app['config']['postgres']
    DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"
    DB_URL = DSN.format(
        user=config['user'],
        password=config['password'],
        database=config['database'],
        host=config['host'],
        port=config['port'],
    )
    pool = await asyncpgsa.create_pool(dsn=DB_URL)
    app['db_pool'] = pool


async def create_job(conn, data):
    await conn.execute(job.insert(data))
