"""
Django settings. Environment specific values are loaded from the environment.
"""
import sys
import os
import re
import dj_database_url
from core.env_utils import parse_emails, bool_value
import datetime

def load_env():
    """
    Load .env file to the environment
    """
    envfile = 'server/.env'

    try:
        with open(envfile) as f:
            content = f.read()
    except IOError:
        print 'error manooo\n'
        content = ''

    for line in content.splitlines():
        m1 = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)
            m3 = re.match(r'\A"(.*)"\Z', val)
            if m3:
                val = re.sub(r'\\(.)', r'\1', m3.group(1))
            os.environ.setdefault(key, val)
load_env()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#CLIENT_BASE_DIR = os.path.join(BASE_DIR, '../client')

SECRET_KEY = os.environ.get('DJANGO_SECRET')
DEBUG = bool_value(os.environ.get('DJANGO_DEBUG'))
ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS = (
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'corsheaders',
    'rest_framework',
    'rest_framework_docs',
    'user',
    'pergunta',
    'jogo',
    'item',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': dj_database_url.config()
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Static file and template locations
# if DEBUG:
#     DJANGO_TEMPLATE_DIRS = (
#         os.path.join(CLIENT_BASE_DIR, 'app'),
#     )

#     STATICFILES_DIRS = (
#         os.path.join(CLIENT_BASE_DIR, 'app', 'static'),
#         os.path.join(CLIENT_BASE_DIR, '.tmp', 'static')  # Generated CSS files
#     )
# else:
#     DJANGO_TEMPLATE_DIRS = (
#         os.path.join(CLIENT_BASE_DIR, 'dist'),
#     )

#     STATICFILES_DIRS = (
#         os.path.join(CLIENT_BASE_DIR, 'dist', 'static'),
#     )
DJANGO_TEMPLATE_DIRS =[]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':DJANGO_TEMPLATE_DIRS ,
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

# Mail
FORM_MAIL = os.environ.get('DJANGO_FROM_MAIL')

if 'SENDGRID_USERNAME' in os.environ:
    EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Custom user
AUTH_USER_MODEL = 'user.Usuario'

# REST API
REST_FRAMEWORK = {
    'UNICODE_JSON': True,
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAdminUser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DEFAULT_RENDERER_CLASSES': (
    #      #UnicodeJSONRenderer has an ensure_ascii = False attribute,
    #      #thus it will not escape characters.
    #     'rest_framework.renderers.UnicodeJSONRenderer',
    #      #You only need to keep this one if you're using the browsable API
    #     'rest_framework.renderers.BrowsableAPIRenderer'
    # )
}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'user.helper.response_User_jwt_payload_handler',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_VERIFY_EXPIRATION' : False,
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=180000),
}

# Logging and error reporting
ADMINS = parse_emails(os.environ.get('DJANGO_ADMINS'))
MANAGERS = parse_emails(os.environ.get('DJANGO_MANAGERS'))

IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
