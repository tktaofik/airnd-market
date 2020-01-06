from sqlalchemy import create_engine, MetaData
from job.db import job
from job.config import get_config

config = get_config()

db_name = config['db_name']
db_port = config['db_port']
db_host = config['db_host']
db_user = config['db_user']
db_password = config['db_password']

admin_engine = create_engine(
    f"postgresql://postgres:postgres@{config['db_host']}:5432/postgres", isolation_level='AUTOCOMMIT')

user_engine = create_engine(
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")


def setup_db():
    conn = admin_engine.connect()
    conn.execute(f"DROP DATABASE IF EXISTS {db_name}")
    conn.execute(f"DROP ROLE IF EXISTS {db_user}")
    conn.execute(f"CREATE USER {db_user} WITH PASSWORD '{db_password}'")
    conn.execute(f"CREATE DATABASE {db_name}")
    conn.execute(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user}")
    conn.close()


def teardown_db():
    conn = admin_engine.connect()
    conn.execute("""
      SELECT pg_terminate_backend(pg_stat_activity.pid)
      FROM pg_stat_activity
      WHERE pg_stat_activity.datname = '%s'
        AND pid <> pg_backend_pid();""" % db_name)
    conn.execute("DROP DATABASE IF EXISTS %s" % db_name)
    conn.execute("DROP ROLE IF EXISTS %s" % db_user)
    conn.close()


def create_tables():
    meta = MetaData()
    meta.create_all(bind=user_engine, tables=[job])


def sample_data():
    conn = user_engine.connect()
    conn.execute(job.insert(), [
        {'userId': 'userId'}
    ])
    conn.close()


if __name__ == '__main__':
    setup_db()
    create_tables()
    print(f"Database initialized")
