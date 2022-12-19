"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import datetime
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

BASE_URL = '/pimages'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s7p0)myu$$wc5b*&ftpc4ocjt27d86ls1bbdkp4yqd%v*+d(g9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
      'adminlte3',
    'adminlte3_theme',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    'rest_framework',
    'rest_framework.authtoken',
    'social_django',

    'loginApp',
    'designApp',
    'personaApp'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', #add this
                'social_django.context_processors.login_redirect', #add this
                
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME' : 'New-DB',
        'CLIENT': {
        'host': 'mongodb+srv://consultrajs:FmjjmzZLsyU1Kxna@cluster0.4z7cbl0.mongodb.net/test'
        
        }
    }
}



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


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}



AUTH_USER_MODEL = 'loginApp.CustomUsersV2'

AUTHENTICATION_BACKENDS = [
    'loginApp.backends.SSOAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
]



# SITE_ID = 1

# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = 'http://127.0.0.1:3000/'
# LOGIN_REDIRECT_URL = 'http://127.0.0.1:3000/'


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT =  os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}


# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:3000',
#     'http://127.0.0.1:3000',
# )

# CSRF_COOKIE_SAMESITE = 'Lex'
# SESSION_COOKIE_SAMESITE = 'Lax'
# CSRF_COOKIE_HTTPONLY = True
# SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SAMESITE = "None"
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE =True
CSRF_COOKIE_SECURE =True

CSRF_TRUSTED_ORIGINS = ['http://localhost:3000','https://ginee.ai','http://13.233.34.229']

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS=True


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='467988292702-89kdb585nfi5kbe42j7kpu5ogb720p5t.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='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'


SOCIAL_AUTH_FACEBOOK_KEY = '1760543307650195'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '95700f659d9b78ecc5bc7e67a39300e3'



EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'srshbtt@gmail.com'
EMAIL_HOST_PASSWORD = 'zobyvfzxbvriwikh'


# **************************PERSONA SETTINGS******************************#

PERSONA_DEVICES = {
    'PDM01' : 'smartphone',
    'PDT02' : 'tablet',
    'PDL03' : 'laptop',
    'PDD04' : 'desktop'
}

PERSONA_SOCIAL = {
    'PSF01' : 'facebook',
    'PST02' : 'twitter',
    'PSI03' : 'instagram',
    'PSP04' : 'pinterest',
    'PSW05' : 'whatsapp',
    'PSY06' : 'youtube',
    'PSS07' : 'snapchat'
}

PERSONA_TECH = {
    'PTW01' : 'windows',
    'PTM02' : 'mac',
    'PTL03' : 'linux',
    'PTA04' : 'android'
}