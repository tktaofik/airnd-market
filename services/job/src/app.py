from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def handle(request):
    return web.Response(text='Hello Aiohttp!')

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
