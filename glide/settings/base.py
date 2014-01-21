import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'g3o7_e)t+xh9u#hrju^ce9exzxivm^u9@mozuxdk1tco!t1xxy'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "glide.core.notifications.notification-processors.notifications",
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'registerforglide@gmail.com'
EMAIL_HOST_PASSWORD = 'RegisterGlide'

AUTH_PROFILE_MODULE = 'profiles.Profile'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'files/uploads')
MEDIA_URL = '/uploads/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'files/static'),
)

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 2

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sorl.thumbnail',
    'markup_deprecated',
    'glide.core',
    'glide.core.profiles',
    'glide.core.notifications',

    'glide.app',
    'glide.app.landing',
    'glide.app.inbox',
    'glide.app.testimonial',
    'glide.app.marketplace',
    'glide.app.interests',
    'glide.app.mission',
    'glide.app.team',
    'glide.app.contact',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'glide.urls'

WSGI_APPLICATION = 'glide.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
