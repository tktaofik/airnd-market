import logging
import sys

from aiohttp import web

from service.routes import routes
from service.db import init_db
from service.config import get_config


async def init_app(config):
    app = web.Application()

    app['config'] = config

    await init_db(app)

    app.add_routes(routes)

    return app


def main():
    config = get_config()

    logging.basicConfig(level=logging.ERROR)

    app = init_app(config)

    web.run_app(app,
                host=config['host'],
                port=config['port'])


if __name__ == '__main__':
    main()
