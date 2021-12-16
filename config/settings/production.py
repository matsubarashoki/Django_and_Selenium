from .base import *

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.application'


#ロギング設定
LOG_BASE_DIR = BASE_DIR / 'config' / 'logs'
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s [%(levelname)s] %(message)s"
        },
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    },
    "handlers": {
        "console": {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
        "info": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_BASE_DIR / "info.log",
            "formatter": "simple",
            "maxBytes": 1024 * 512 * 1,  # 1 MB, 
            "backupCount": 5
        },
        "warning": {
            "level": "WARNING",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_BASE_DIR / "warning.log",
            "formatter": "simple",
            "maxBytes": 1024 * 512 * 1,  # 1 MB, 
            "backupCount": 5
        },
        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_BASE_DIR / "error.log",
            "formatter": "simple",
            "maxBytes": 1024 * 512 * 1,  # 1 MB, 
            "backupCount": 5
        }
    },
    "loggers": {
        'django':{
            "handlers": ["info", "warning", "error"],
            "level": "INFO",
        },
        'youtube_text':{
            "handlers": ["info", "warning", "error"],
            "level": "INFO",
        },
        'blog':{
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    },
}