# -*- coding: utf8 -*-
import os
import sys
gettext = lambda s: s

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Debug
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

ALLOWED_HOSTS = [
    '*'
]

# Caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Local time zone for this installation.
TIME_ZONE = 'America/Chicago'

# Language code for this installation.
LANGUAGE_CODE = 'ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Static and Media files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'blog_test', 'static'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&c5x5-u9u$#eet2c1irn4e2*^r(px-#af)6v@4ux18g!a$!k_&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# debug_toolbar
#DEBUG_TOOLBAR_PATCH_SETTINGS = False
#INTERNAL_IPS = (
#    '192.168.133.1',
#    '127.0.0.1',
#)

MIDDLEWARE_CLASSES = (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug_toolbar
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blog_test.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'blog_test.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'blog_test', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
)

# easy_thumbnails
from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'ifcropper.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

INSTALLED_APPS = (
    # ===== django ===== #
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # ===== vendors ==== #
    #'debug_toolbar',
    'easy_thumbnails',
    'south',
    'tinymce',
    'django_bootstrap_breadcrumbs',
    'captcha',

    # === blog_test === #
    'ifcropper',
    'blog',
)

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'width': 850,
    'height': 400,
}

#CAPTCHA settings
CAPTCHA_FONT_SIZE = 30
#CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.word_challenge'
#CAPTCHA_NOISE_FUNCTIONS = ''
#CAPTCHA_FILTER_FUNCTIONS = ''
if 'test' in sys.argv:
    CAPTCHA_TEST_MODE = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 'NAME': u'simplelife_test', 'HOST': u'localhost', 'USER': u'root', 'PASSWORD': u'12345', 'PORT': '',
        'TEST_CHARSET': 'utf8', 'TEST_COLLATION': 'utf8_unicode_ci'
    }
}
