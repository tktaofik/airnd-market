import os
from aiohttp import web
from server.routes import routes


def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, port=os.getenv("PORT", 8081))


if __name__ == '__main__':
    main()
