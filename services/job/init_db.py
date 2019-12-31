from sqlalchemy import create_engine, MetaData

from service.db import job
from service.config import BASE_DIR, get_config


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

ADMIN_DB_URL = DSN.format(
    user='postgres', password='postgres', database='postgres',
    host='localhost', port=5432
)

admin_engine = create_engine(ADMIN_DB_URL, isolation_level='AUTOCOMMIT')

CONFIG_PATH = BASE_DIR / 'config' / 'job.yaml'
CONFIG = get_config(['-c', CONFIG_PATH.as_posix()])
DB_URL = DSN.format(**CONFIG['postgres'])

engine = create_engine(DB_URL)
config = CONFIG['postgres']


def setup_db():
    db_name = config['database']
    db_user = config['user']
    db_pass = config['password']

    conn = admin_engine.connect()
    conn.execute(f"DROP DATABASE IF EXISTS {db_name}")
    conn.execute(f"DROP ROLE IF EXISTS {db_user}")
    conn.execute(f"CREATE USER {db_user} WITH PASSWORD '{db_pass}'")
    conn.execute(f"CREATE DATABASE {db_name}")
    conn.execute(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user}")
    conn.close()


def teardown_db():
    db_name = config['database']
    db_user = config['user']

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
    meta.create_all(bind=engine, tables=[job])


def sample_data():
    conn = engine.connect()
    conn.execute(job.insert(), [
        {'userId': 'userId'}
    ])
    conn.close()


if __name__ == '__main__':
    setup_db()
    create_tables()
    sample_data()
    print(f"Database initialized with sample data DB_URL: {DB_URL}")
