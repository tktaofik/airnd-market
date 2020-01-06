import os

from dotenv import load_dotenv

load_dotenv()


def get_config():
    return {
        "port": os.getenv('PORT'),
        "postgres": {
            "database": os.getenv('DATABASE'),
            "user": os.getenv('DB_USER'),
            "password": os.getenv('DB_PASSWORD'),
            "host": os.getenv('DB_HOST'),
            "port": os.getenv('DB_PORT'),
            "minsize": os.getenv('DB_POOL_MIN_SIZE'),
            "maxsize": os.getenv('DB_POOL_MAX_SIZE'),
        }
    }
