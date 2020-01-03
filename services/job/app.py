import logging
import sys

from aiohttp import web

from service.routes import routes
from service.db import init_db
from service.config import get_config

config = get_config()


async def init_app():
    logging.basicConfig(level=logging.INFO)

    app = web.Application()
    app['config'] = config
    app.add_routes(routes)

    await init_db(app)

    return app

if __name__ == '__main__':
    app = init_app()
    web.run_app(app, host=config['host'], port=config['port'])
