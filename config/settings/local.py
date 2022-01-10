from .base import *

DEBUG = True


#問い合わせフォームでメール送信するための設定コンソール出力する
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# バックアップバッチ用
BACKUP_PATH = str(os.path.join(BASE_DIR, 'backup/'))
NUM_SAVED_BACKUP = 2

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'local': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'local',
        },
    },
    'loggers': {
        # 自作したログ出力
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # 実行SQL
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
