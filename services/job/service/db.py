import enum

import aiopg.sa

from datetime import datetime

from sqlalchemy import (
    create_engine, MetaData, Table, Column, ForeignKey,
    Integer, String, Date, Enum
)


# session should be recreated
# https://stackoverflow.com/questions/12223335/sqlalchemy-creating-vs-reusing-a-session

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


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
