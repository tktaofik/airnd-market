import enum
import json

from datetime import datetime
from asyncpgsa import pg

from sqlalchemy import (
    create_engine, MetaData, Table, Column, ForeignKey,
    Integer, String, DateTime, Enum, literal_column
)

# LINKS:

# why session should be recreated
# https://stackoverflow.com/questions/12223335/sqlalchemy-creating-vs-reusing-a-session

# python-sqlalchemy
# https://www.pythonsheets.com/notes/python-sqlalchemy.html#insert-create-an-insert-statement

# sqlalchemy Data types
# https://www.oreilly.com/library/view/essential-sqlalchemy/9780596516147/ch04.html

# asyncpgsa
# https://asyncpgsa.readthedocs.io/en/latest/#


meta = MetaData()


class Status(enum.Enum):
    new = "new"
    inProgress = "inProgress"
    cancelled = "cancelled"
    done = "done"


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
    Column("createdAt", DateTime, default=datetime.utcnow()),
    Column("updatedAt", DateTime, default=datetime.utcnow())
)


async def init_db(app):
    config = app['config']['postgres']
    await pg.init(
        host=config['host'],
        port=config['port'],
        database=config['database'],
        user=config['user'],
        password=config['password'],
        min_size=1,
        max_size=10,
    )


async def create_job(data):
    stm = job.insert(data).returning(literal_column("*"))
    row = await pg.fetchrow(stm)
    return dict(row)
