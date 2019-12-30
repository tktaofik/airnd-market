import os
from aiohttp import web
from server.routes import routes

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, port=os.getenv("PORT", 8081))
