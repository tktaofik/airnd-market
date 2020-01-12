from aiohttp import web
from job.routes import routes
from job.middlewares import error_middleware
from job.db import init_db
from job.config import get_config

import logging
import sentry_sdk

from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

sentry_sdk.init(
    # Make sure to use the right Sentry key
    dsn=f"http://fffb69fb4cb743e0ac982183235ce2a7@0.0.0.0:1234/2",
    integrations=[
        LoggingIntegration(level=logging.DEBUG, event_level=logging.INFO),
        AioHttpIntegration(),
        SqlalchemyIntegration(),
    ]
)


async def init_app(config):
    middlewares = [error_middleware]

    app = web.Application(middlewares=middlewares)

    app['config'] = config

    await init_db(app)

    app.add_routes(routes)

    return app


def main():
    config = get_config()

    logging.basicConfig(level=logging.DEBUG)

    app = init_app(config)

    web.run_app(app, port=config['port'])


if __name__ == '__main__':
    main()
