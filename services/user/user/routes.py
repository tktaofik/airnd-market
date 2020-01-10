from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/ready')
async def ready_handler(request: web.Request):
    return web.json_response(status=200)
