"""
Django settings. Environment specific values are loaded from the environment.
"""

import sys
import os
import re
import dj_database_url
from core.env_utils import parse_emails, bool_value

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
# OR, the same with increased verbosity:
# load_dotenv(dotenv_path, verbose=True)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#CLIENT_BASE_DIR = os.path.join(BASE_DIR, '../client')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool_value(os.environ.get('DJANGO_DEBUG'))

# Honor the 'Host' header
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'corsheaders',
    'rest_framework',
    'rest_framework_docs',
    'accounts',
    'api'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
)
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'


# Parse database configuration from $DATABASE_URL
DATABASES = {
    'default': dj_database_url.config()
}


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

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
AUTH_USER_MODEL = 'accounts.BaseUser'

# REST API
REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAdminUser'
        'rest_framework.permissions.AllowAny'
    ]
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