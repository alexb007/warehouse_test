import asyncio

from WarehouseTest.celery import app
from store.api_calls import create_order


@app.task(name='create_order')
def create_order(order_json):
    asyncio.run(create_order(order_json))
