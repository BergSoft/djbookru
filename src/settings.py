# -*- coding: utf-8 -*-

import os, sys, glob


def PROJECT_DIR(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PUBLIC_DIR = PROJECT_DIR('public')


# get local software repositories
sys.path.insert(0, PROJECT_DIR('..', 'lib'))
gettext_noop = lambda s: s


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': dict(
        ENGINE='django.db.backends.mysql',
        NAME='djbookru',
        USER='djbookru',
        PASSWORD='q1',
        HOST='localhost',
        PORT='',
        )
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'
# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True
USE_THOUSAND_SEPARATOR = True
LOCALE_PATHS = (
    PROJECT_DIR('main', 'locale'),
)

SITE_ID = 1
SITE_URL = 'http://djbook.ru/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PUBLIC_DIR('media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = PUBLIC_DIR('static')
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'pagination.middleware.PaginationMiddleware',
    'djangobb_forum.middleware.LastLoginMiddleware',
    'djangobb_forum.middleware.UsersOnline',
)

ROOT_URLCONF = 'src.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'src.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',

    'context_processors.custom',
    'adzone.context_processors.get_source_ip',
    'social_auth.context_processors.social_auth_backends',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR('templates'),
)

FIXTURE_DIRS = (
    PROJECT_DIR('fixtures'),
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'plain': {
            'format': '%(asctime)s %(message)s',
        },
        'verbose': {
            'format':
                '%(levelname)s %(asctime)s %(name)s %(process)d %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'main_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR('..', 'logs', 'main.log'),
            'maxBytes': 1024 * 1024 * 1,
            'backupCount': 10,
            'formatter': 'verbose',
        },
        'haystack_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR('..', 'logs', 'haystack.log'),
            'maxBytes': 1024 * 1024 * 1,
            'backupCount': 5,
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'haystack': dict(
            handlers=['haystack_log'],
            level='ERROR',
            propagate=True,
        ),
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.flatpages',

    'adzone',
    'bootstrapform'
    'chunks',
    'google_analytics',
    'oembed',
    'pagination',
    'robots',
    'sorl.thumbnail',
    'tagging',

    'accounts',
    'claims',
    'comments',
    'doc_comments',
    'examples',
    'main',
    'news',
    'utils',
    'videos',
)


### AUTH: BEGIN
LOGIN_URL = '/auth/login/'
LOGIN_ERROR_URL = LOGIN_URL
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

OPENID_REDIRECT_NEXT = '/socialauth/openid/done/'

OPENID_SREG = {"required": "nickname, email", "optional": "postcode, country", "policy_url": ""}
OPENID_AX = [{"type_uri": "http://axschema.org/contact/email", "count": 1, "required": True, "alias": "email"},
             {"type_uri": "fullname", "count": 1, "required": False, "alias": "fullname"}]

TWITTER_CONSUMER_KEY = 'see production settings'
TWITTER_CONSUMER_SECRET = 'see production settings'
### AUTH: END


### SOCIAL_AUTH: BEGIN
INSTALLED_APPS += ('social_auth', )
SOCIAL_AUTH_USER_MODEL = 'accounts.User'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_PROCESS_EXCEPTIONS = 'social_auth.utils.log_exceptions_to_messages'
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.user.get_username',
    'accounts.social_auth_pipelines.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
)
GITHUB_APP_ID = 'see production settings'
GITHUB_API_SECRET = 'see production settings'

### SOCIAL_AUTH: BEGIN


### ADMIN-TOOLS: BEGIN
INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    ) + INSTALLED_APPS
ADMIN_TOOLS_INDEX_DASHBOARD = 'src.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'src.dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_MENU = 'src.menu.CustomMenu'
ADMIN_MEDIA_PREFIX = '/static/admin/'  # грязный хак
### ADMIN-TOOLS: END


### HAYSTACK: BEGIN
def get_doc_pages(path, ext):
    for directory, dirnames, filenames in os.walk(path):
        for item in glob.glob('%s/*.%s' % (directory, ext)):
            yield item

DJANGO_DOCUMENTATION_URL = '/rel1.4/'

INSTALLED_APPS += ('haystack', 'haystack_static_pages')
HAYSTACK_SITECONF = 'search_sites'
HAYSTACK_SEARCH_ENGINE = 'xapian'
HAYSTACK_XAPIAN_PATH = PROJECT_DIR('search_index')
HAYSTACK_STATIC_PAGES = tuple(
    get_doc_pages(
        os.path.expanduser('~/devel/django_documentation/_build/html'),
        'html'))
HAYSTACK_STATIC_MAPPING = {
    os.path.expanduser('~/devel/django_documentation/_build/html'): 'http://127.0.0.1:8000/rel1.4'
    }
### HAYSTACK: END


### FEEDBACK: BEGIN
EMAIL_SUBJECT_PREFIX = '[Djbook.ru]'
DATETIME_FORMAT = 'j N Y, G:i'
FEEDBACK_SUBJECT = gettext_noop(u'Feedback message from Djbook.ru')
FEEDBACK_EMAIL = 'djbook.feedback@gmail.com'
### FEEDBACK: END


### SOUTH: BEGIN
INSTALLED_APPS += ('south', )
SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False
### SOUTH: END


### FORUM: BEGIN
INSTALLED_APPS += ('djangobb_forum', )
TOPIC_PAGE_SIZE = 10
REPLY_PAGE_SIZE = 20
FLOOD_TIME = 5
RANKS_NAMES_DATA = ((30, "Member"), (100, "Senior Member"), (300, 'Star'))
### FORUM: BEGIN
