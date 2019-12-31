from init import get_database_engine, user, password, host, port
from model import job


def add_sample_data(engine):
    conn = engine.connect()
    conn.execute(job.insert(), [
        {'userId': 'sdfw23dwed23d'}
    ])
    conn.close()


if __name__ == '__main__':
    db_url = f"postgresql://{user}:{password}@{host}:{port}/job-service"
    engine = get_database_engine(db_url)
    add_sample_data(engine)
    print("Added sample data to job-service job table")
