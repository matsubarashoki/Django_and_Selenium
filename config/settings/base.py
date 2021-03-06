import os
import environ
from pathlib import Path
from django.contrib.messages import constants as messages

# プロジェクト配置ディレクトリ
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
#ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_setting.apps.User_SettingConfig',
    'youtube_text.apps.YoutubeTextConfig',
    'blog.apps.BlogConfig',
    #認証機能用
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account'
    'makepdf.apps.MakepdfConfig',
    'Ajax_test.apps.AjaxTestConfig',
    #modal用
    'bootstrap_modal_forms',
    'widget_tweaks',
    #'django.contrib.humanize'#三桁カンマ
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #ログイン処理強制用モジュール
    'global_login_required.GlobalLoginRequiredMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #ルートのtemplatesから読み込ませる
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

#デフォルト設定
DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
    # 'default':{
    #     'ENGINE':'django.db.backends.postgresql_psycopg2',
    #     'NAME':'youtube_text',
    #     'USER':'youtube_text',
    #     'PASSWORD':'54321',
    #     'HOST':'127.0.0.1',
    #     'POST':'5432'
    # }
    'default' : env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Userモデルの代わりにCustomUserモデルを使用するための設定
AUTH_USER_MODEL = 'user_setting.CustomUser'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#from . import newsapi
#newsapi.NEWS_API
NEWSAPI = env('NEWS_API')

#ログイン強制しないパス
PUBLIC_PATHS = [
    '/login',
    '/signup',
    '/signup_success'
]

#BootStrap Alertsでメッセージの見た目適用
MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}
