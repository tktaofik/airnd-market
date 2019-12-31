import os
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import (MetaData, create_engine)
from model import job

user = os.getenv("POSTGRES_USER", "root")
password = os.getenv("POSTGRES_PASSWORD", "password")
host = os.getenv("POSTGRES_HOST", "localhost")
port = os.getenv("POSTGRES_PORT", 5432)


def get_database_engine(db_url):
    engine = create_engine(db_url)
    if not database_exists(engine.url):
        create_database(engine.url)
    return engine


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[job])
    print("Database table job created")


if __name__ == '__main__':
    db_url = f"postgresql://{user}:{password}@{host}:{port}/job-service"
    engine = get_database_engine(db_url)
    create_tables(engine)
    print(f"Database created: {db_url}")
