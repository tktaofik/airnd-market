import logging
import sys

from aiohttp import web

from service.routes import routes
from service.db import init_db
from service.config import get_config


async def init_app(argv=None):

    app = web.Application()

    # save app config in app
    app['config'] = get_config(argv)

    # create db pool connection
    await init_db(app)

    # setup  routes
    app.add_routes(routes)

    return app


def main(argv):
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(argv)

    config = get_config(argv)
    web.run_app(app,
                host=config['host'],
                port=config['port'])


if __name__ == '__main__':
    main(sys.argv[1:])
