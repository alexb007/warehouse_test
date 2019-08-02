from django.conf import settings

REDIS_HOST = settings.ENVIRON.str('REDIS_HOST', default='redis')
REDIS_PORT = settings.ENVIRON.str('REDIS_PORT', default='6379')
REDIS_PASSWORD = settings.ENVIRON.str('REDIS_PASSWORD', default='')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [
            'redis://{}:{}/1'.format(REDIS_HOST, REDIS_PORT)
        ],
        'OPTIONS': {

        }
    },
}

if REDIS_PASSWORD:
    CACHES['default']['OPTIONS']['PASSWORD'] = REDIS_PASSWORD
