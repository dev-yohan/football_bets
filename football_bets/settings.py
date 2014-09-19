"""
Django settings for football_bets project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ba6nu_ml_r^=uv(54%sgi#1i)j9qs5zcnzhr76872=ir5ym=c-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'djangotoolbox',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'social.apps.django_app.me',
    'django_evolution',
    'cloudinary',
    'teams',
    'leagues',
    'matches'
)

#SOCIAL_AUTH_MODELS = 'social_auth.db.mongoengine_models'
#SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)



TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',                            
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

ROOT_URLCONF = 'football_bets.urls'
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_FACEBOOK_KEY = '1473216766284607'
SOCIAL_AUTH_FACEBOOK_SECRET = '65c541f6cd63501da2bb036b85520e73'

WSGI_APPLICATION = 'football_bets.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'football_bets',
        'HOST':'localhost',
        'PORT': 27017,
    }
}

from mongoengine import connect
connect('football_bets')

SITE_ID = '541b28dde565cc2c944b155d'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

cloudinary.config(
  cloud_name = "dfvucpnfl",
  api_key = "295135318988452",
  api_secret = "IvCf10cKUtkabhtDMCFe-Zs4LzM"
)

