# Test Warehouse App

Deploy:
* Create `.env` file under project root folder. Fill it as `.env.example` file.
* Run `python manage.py migrate`
* Create superuser `python manage.py createsuperuser`

Run django:
``python manage.py runserver``

Run celery worker:
`celery worker -A WarehouseTest -E`
