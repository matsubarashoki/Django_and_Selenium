from typing import Pattern
from django.core.exceptions import ValidationError
import re
import logging
#バリデーション専用ファイル
#独自バリデーションをつくってformsやmodelで連携するらしい
#これとは別にformsにcleanメソッドでの方法もあるがFormsにしかできない

#ロギングオブジェクト生成
logger = logging.getLogger('youtube_text')


#URLがyoutubeのものかのバリデーション

#正規表現オブジェクト生成
Pattern = '^https://www.youtube.com/watch'

def validate_url(value):
    if not re.match(Pattern,value):
        logger.warning('不正なURL:' + value)
        raise ValidationError('Youtubeのリンクではありません。')