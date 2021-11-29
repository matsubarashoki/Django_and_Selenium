from django.db import models
from django.forms import ModelForm, fields
from .models import SearchLog

class SearchLogForm(ModelForm):
    '''実行履歴モデルのフォーム'''

    class Meta:
        '''
        Attributes:
            model:モデルのクラス
            fields:フォームで使用するモデルのフィールドを指定
        '''
        model = SearchLog
        fields = ['title','url','result']