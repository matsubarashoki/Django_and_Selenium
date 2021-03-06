from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.core.mail import EmailMessage
from .models import BlogPost, Comment

class BlogPostForm(ModelForm):
    '''記事 Airticleのモデルフォーム'''
    class Meta:
        model = BlogPost
        fields = ['title','content']

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = '記事のタイトル'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = '記事本文'
        self.fields['content'].widget.attrs['class'] = 'form-control'


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
        self.fields['comment'].widget.attrs['placeholder'] = 'コメントを入力してください'
        self.fields['comment'].widget.attrs['class'] = 'form-control'

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル',max_length=30)
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください'
        
        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください'
    
    def send_email(self):
        #cleande_dataはバリデーション
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ{}'.format(title)
        message = '送信者: {0}\nメールアドレス:{1}\nメッセージ：{2}'.format(name,email,message)
        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
        ]
        cc_list = [
            email
        ]
        #DjangoのEmail機能を活用してメール送信
        message = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=to_list,
            cc=cc_list
        )
        message.send()