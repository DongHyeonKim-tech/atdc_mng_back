from .base import *
environ.Env.read_env(os.path.join(BASE_DIR, 'env/.env.dev'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']


CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        'HOST' : env('DATABASE_HOST'),
        'PORT' : env('DATABASE_PORT')
    }
}