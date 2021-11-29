from django.db import models
from django.forms import ModelForm, fields
from .models import Comment

class CommentForm(ModelForm):
    '''Commentモデルのフォーム'''

    class Meta:
        '''
        Attributes:
            model:モデルのクラス
            fields:フォームで使用するモデルのフィールドを指定
        '''
        model = Comment
        fields = ['comment']
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)