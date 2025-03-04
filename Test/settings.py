import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=^#e$%9nkp%03y9az!xn6(tw$n&^env1$er0_l-6t#ziseza87'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

INSTALLED_APPS = [
    'jazzmin',
    'debug_toolbar',
    'django.contrib.admin',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounting',
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

JAZZMIN_SETTINGS = {
    "custom_css": "css/jazzmin-fixes.css",
    "site_title": "Comptabilité API",
    "site_header": "Comptabilité API",
    "site_brand": "Comptabilité",
    "site_logo": "logo.png",
    "login_logo": "logo.png",
    "login_logo_dark": "logo.png",
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Bienvenue sur le panneau d'administration de l'API de gestion comptable",
    "user_avatar": None,
    "show_ui_builder": False,
    "navigation_expanded": True,
    "copyright": "j0shu4",
    "search_model": ["auth.User", "auth.Group"],
    "topmenu_links": [
        {"name": "Accueil", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    "custom_links": {
        "books": [{
            "name": "Créer des messages", "url": "make_messages", "icon": "fas fa-comments", "permissions": ["books.view_book"]
        }]
    },
    "icons": {
        "auth": "fas fa-shield-alt",
        "auth.user": "fas fa-user-tie",
        "auth.Group": "fas fa-users-cog",
        "utilisateurs": "fas fa-user-friends",
        "gestion": "fas fa-cogs",
        "new_model": "fas fa-new-icon",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": "css/custom.css",
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
    },
}
JAZZMIN_UI_TWEAKS = {
    "theme": "litera",
    "dark_mode_theme": "darkly",
}

# settings.py

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Format: Bearer <token>'
        }
    },
    'USE_SESSION_AUTH': False,
}


ROOT_URLCONF = 'Test.urls'
INTERNAL_IPS = [
    '127.0.0.1'
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

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

WSGI_APPLICATION = 'Test.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

# Database postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'comptabilite',
        'USER': 'db_admin_test',
        'PASSWORD': 'compt2@25Benin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
