import aiohttp
from aiohttp import web
adv = {}
adv_id = 1
async def create_ad(request):
    global adv_id
    inf = await request.json()
    inf_adv = {
        'id': adv_id,
        'title': inf['title'],
        'description': inf['description'],
        'date': inf['date'],
        'name': inf['name']

    }
    adv[adv_id] = inf_adv
    adv_id += 1
    return web.json_response(inf_adv, status = 201)
async def get_adv(request):
    return web.json_response(list(adv.values()))
async def delete_adv(request):
    adv_user_id = int(request.match_info['id'])
    if adv_user_id in adv:
        del adv[adv_user_id]
        return web.json_response({'message': 'Obyavlenie udaleno'}, status = 200)
    return web.json_response({'error': 'chto to poshlo ne tak'}, status = 404)
r = web.Application()
r.router.add_post('/adv', create_ad)       
r.router.add_get('/adv', get_adv)
r.router.add_delete('/adv/{id}', delete_adv)
web.run_app(r, host = '127.0.0.1', port = 8080)