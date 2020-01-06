from sqlalchemy import create_engine, MetaData
from job.config import get_config

config = get_config()

db_name = config['db_name']
db_port = config['db_port']
db_host = config['db_host']
db_user = config['db_user']

admin_engine = create_engine(
    f"postgresql://postgres:postgres@{config['db_host']}:5432/postgres", isolation_level='AUTOCOMMIT')


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


if __name__ == '__main__':
    teardown_db()
    print(f"Database removed")
