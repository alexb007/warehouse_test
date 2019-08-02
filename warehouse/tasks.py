from WarehouseTest.celery import app
from warehouse.api_calls import update_order_call, delete_order_call


@app.task
def update_order(order):
    print('calling api')
    update_order_call(order)


@app.task
def delete_order(order_id):
    print('calling delete api')
    delete_order_call(order_id)
