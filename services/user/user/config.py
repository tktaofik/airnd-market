import os

from dotenv import load_dotenv

load_dotenv()


def get_config():
    return {
        "port": os.getenv('PORT'),
        "sentry_key": os.getenv('SENTRY_KEY'),
    }
