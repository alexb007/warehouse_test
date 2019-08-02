import aiohttp
import asyncio

from django.conf import settings


async def _make_request(url, data, method='POST'):
    headers = {
        'Authorization': settings.STORE_API_KEY
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        if method == 'POST':
            return await session.post(url, json=data)
        elif method == 'UPDATE':
            return await session.put(url, data=data)
        elif method == 'DELETE':
            return await session.delete(url)


def make_request(url, data, method='POST'):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(_make_request(url, data, method))
    loop.close()


def update_order_call(order):
    if 'id' in order:
        make_request("{}/orders/{}/".format(settings.STORE_API_URL, order.get('id')), order, 'UPDATE')
    return 'Bad Request'


def delete_order_call(order_id):
    make_request("{}/orders/{}/".format(settings.STORE_API_URL, order_id), None, 'DELETE')
