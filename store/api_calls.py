import aiohttp

from django.conf import settings


async def create_order(order_json):
    async with aiohttp.ClientSession() as session:
        await session.post("{}/orders/".format(settings.WAREHOUSE_API_URL), json=order_json)
