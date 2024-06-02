from pathlib import Path
import os
from configurations import Configuration, values
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

class Dev(Configuration):
    SECRET_KEY = "django-insecure-ym=d)ft4%)xiukqr&tgstl6i2091+x_#&o%*%n6g^epgy(bpd6"
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    
    # Security Settings
    X_FRAME_OPTIONS = 'ALLOW-FROM ' + os.environ.get('CODIO_HOSTNAME', '') + '-8000.codio.io'
    CSRF_COOKIE_SAMESITE = None
    CSRF_TRUSTED_ORIGINS = [os.environ.get('CODIO_HOSTNAME', '') + '-8000.codio.io']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SAMESITE = 'None'

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',  # Ensure this line is present
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'crispy_forms',
        'crispy_bootstrap5',
        'debug_toolbar',
        'blog',
    ]

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    INTERNAL_IPS = ["192.168.11.51"]
    ROOT_URLCONF = 'blango.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
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

    WSGI_APPLICATION = 'blango.wsgi.application'

    # Database
    DATABASES = {
        'default': dj_database_url.config(default=f"sqlite:///{BASE_DIR}/db.sqlite3"),
    }
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]

    # Password validation
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
    ]

    # Internationalization
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = values.Value("UTC")
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'

    # Default primary key field type
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    # Crispy Forms
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"

    DJANGO_ADMINS="Admin, the.admin@gmail.com;"

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse",
            },
        },
        "formatters": {
            "verbose": {
                "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "verbose",
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
                "filters": ["require_debug_false"],
            },
        },
        "loggers": {
            "django.request": {
                "handlers": ["mail_admins"],
                "level": "ERROR",
                "propagate": True,
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    }