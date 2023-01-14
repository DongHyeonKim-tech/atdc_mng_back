import os
from pathlib import Path
from datetime import timedelta
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, 'env/.env'))

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# 유저모델 사용 지정
AUTH_USER_MODEL = 'authority.User'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',

    # local app
    'conn_test',
    'teams',
    'members',
    'authority',
    'attendance',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # 반드시 middleware.common.CommonMiddleware 위쪽에 작성
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [ # 기본적인 view 접근 권한 지정
        'rest_framework.permissions.AllowAny', # FIXME: rest_framework.permissions.IsAuthenticated
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [ # token을 인증할 클래스 설정
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PARSER_CLASSES' : [ # request.data 속성에 액세스 할 때 사용되는 파서 지정
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ]
}



SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME' : timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME' : timedelta(days=1),
    'ROTATE_REFRESH_TOKEN': False,  # True면 TokenRefreshView시 새로운 토큰을 반환
    'BLACKLIST_AFTER_ROTATE' : False,
    'UPDATE_LAST_LOGIN' : True, # True면 로그인시 auth_user테이블의 last_login필드가 업데이트 됨

    'ALGORITHM' : "HS256",
    'SIGNING_KEY' : SECRET_KEY,
    'AUDIENCE' : None,
    'ISSUER' : None,
    'JWT_URL' : None,
    'LEEWAY' : 0,

    'AUTH_HEADER_TYPES' : ('Bearer',),
    'AUTH_HEADER_NAME' : 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD' : 'user_id', # 아이디 식별을 위한 auth_user 테이블의 컬럼 이름
    'USER_ID_CLAIM' : 'user_id',
    'USER_AUTHENTICATIONS_RULE' :'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES' : ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM' : 'token_type',
    'TOKEN_USER_CLASS' : 'test_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM' : 'jti'
}


# CORS_ALLOWED_ORIGINS = ['*']
