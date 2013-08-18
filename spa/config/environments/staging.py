from spa.config.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='what.is.cupidon@gmail.com'
EMAIL_HOST_PASSWORD='blahblah'
EMAIL_USE_TLS =True
DEFAULT_FROM_EMAIL ='what.is.cupidon@gmail.com'

# settings/local.py is ignored to allow for easy settings
# overrides without affecting others
try:
    from local import *
except ImportError:
    pass


#########################
# Amazon S3 credentials #
#########################
S3_BUCKET = ""
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
