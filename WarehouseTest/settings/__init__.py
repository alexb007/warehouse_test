import environ
from split_settings.tools import optional, include

root = environ.Path(__file__) - 3
environ.Env.read_env(root('.env'))

SITE_ROOT = root() + '/'
ENVIRON = environ.Env()
DEBUG = ENVIRON.bool('DEBUG', default=False)
CONFIG_NAME = ENVIRON.str('DJANGO_ENV', default='development')


base_settings = [
    'components/base.py',
    'components/middleware.py',
    'components/cors.py',
    'components/database.py',
    'components/cache.py',
    'components/celery.py',
    'components/rest_api.py',
    'components/auth.py',
    'components/logging.py',
    'environments/%s.py' % CONFIG_NAME,
    optional('environments/local.py'),
]

include(*base_settings)
