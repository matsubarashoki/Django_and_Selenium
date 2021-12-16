from .base import *

DEBUG = True


#問い合わせフォームでメール送信するための設定コンソール出力する
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# バックアップバッチ用
BACKUP_PATH = str(os.path.join(BASE_DIR, 'backup/'))
NUM_SAVED_BACKUP = 2
