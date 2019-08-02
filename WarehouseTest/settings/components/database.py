from django.conf import settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': settings.ENVIRON.str('POSTGRES_DB', default='crm'),
        'USER': settings.ENVIRON.str('POSTGRES_USER', default=''),
        'PASSWORD': settings.ENVIRON.str('POSTGRES_PASSWORD', default=''),
        'HOST': settings.ENVIRON.str('POSTGRES_HOST', default=''),
        'PORT': settings.ENVIRON.str('POSTGRES_PORT', default=''),
    }
}
