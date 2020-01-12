import enum
import json

from uuid import uuid4
from datetime import datetime
from asyncpgsa import pg
from sqlalchemy import (
    create_engine, MetaData, Table, Column, ForeignKey,
    Integer, String, DateTime, Enum, literal_column
)
from sqlalchemy.dialects.postgresql import UUID


meta = MetaData()


class UserTypes(enum.Enum):
    client = "client"
    rider = "rider"


user = Table(
    'user', meta,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
    Column("firstName", String),
    Column("lastName", String),
    Column("email", String),
    Column("password", String),
    Column("type", Enum(UserTypes), default=UserTypes.client),
    Column("createdAt", DateTime, default=datetime.utcnow()),
    Column("updatedAt", DateTime, default=datetime.utcnow())
)


async def init_db(app):
    config = app['config']
    await pg.init(
        host=config['db_host'],
        port=config['db_port'],
        user=config['db_user'],
        password=config['db_password'],
        min_size=1,
        max_size=10,
    )


async def create_user(data):
    stm = user.insert(data).returning(literal_column("*"))
    row = await pg.fetchrow(stm)
    created_user = dict(row)
    del created_user['password']
    return created_user


async def get_user(id):
    stm = user.select().where(user.c.id == id)
    row = await pg.fetchrow(stm)
    if row == None:
        return None
    return dict(row)


async def delete_user(id):
    stm = user.delete().where(user.c.id == id)
    await pg.fetchrow(stm)
