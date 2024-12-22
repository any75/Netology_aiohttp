import aiohttp, asyncio
url = 'http://127.0.0.1:8080/adv'
adv_to_create = [
    {'title': 'Продаю телефон', 
    'description': 'б/у телефон отдам недорого',
    'date': '13.12.2024',
    'name': 'Svetlana'},
    {'title': 'Меняю телефон', 
    'description': 'на айфон 16',
    'date': '12.12.2024',
    'name': 'Olga'}
    ]
async def create_adv():
    async with aiohttp.ClientSession() as session:
        for i in adv_to_create:
            async with session.post(url, json = i) as response_post:
                print(response_post.status)
                print(await response_post.json())
        print()
        async with session.get(url) as response_get:
            print(response_get.status)
            print(await response_get.json())
        adv_id = 1
        async with session.delete(f'{url}/{adv_id}') as response_delete:
            if response_delete.status == 200:
                response_data = await response_delete.json()
                print(response_data.get('message', 'Obyavlenie udaleno'))
            else:
                print('Obyavlenie ne udaleno', await response_delete.text())
asyncio.run(create_adv())                