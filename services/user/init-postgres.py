from sqlalchemy import create_engine, MetaData
from user.db import user
from user.config import get_config

config = get_config()

db_name = config['db_name']
db_port = config['db_port']
db_host = config['db_host']
db_user = config['db_user']
db_password = config['db_password']

engine = create_engine(
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}", isolation_level='AUTOCOMMIT')


def setup_db():
    meta = MetaData()
    meta.drop_all(bind=engine, tables=[user])
    meta.create_all(bind=engine, tables=[user])


def add_sample_data():
    conn = engine.connect()
    conn.execute(user.insert(), [
        {
            "firstName": "firstName",
            "lastName": "lastName",
            "email": "email@email.com",
            "password": "password",
            "type": "client",
            "disabled": False,
        }
    ])
    conn.close()


if __name__ == '__main__':
    setup_db()
    add_sample_data()
    print(f"Database initialized")
