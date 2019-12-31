import enum
from datetime import datetime
from sqlalchemy import (
    MetaData, Table, Column,
    Integer, Enum, String, Date
)

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
    Column('pickupAddress', String),
    Column('dropoffAddress', String),
    Column('description', String),
    Column('createdAt', Date, default=datetime.now()),
    Column('updatedAt', Date, default=datetime.now())
)
