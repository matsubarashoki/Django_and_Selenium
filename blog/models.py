from django.db import models
from user_setting.models import CustomUser


# Create your models here.
class BlogPost(models.Model):
    '''ブログmodel postは記事の意味'''

    title = models.CharField(
        'タイトル',
        max_length=200
    )
    content = models.TextField(
        '本文'
    )
    posted_at = models.DateTimeField(
        '投稿日',
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    '''感想コメントmodel'''
    blogpost = models.ForeignKey(
        BlogPost,
        verbose_name='記事',
        related_name='comments',
        on_delete=models.CASCADE,
    )
    comment = models.TextField(
        'コメント',
    )
    posted_at = models.DateTimeField(
        '投稿日',
        auto_now_add=True
    )
    #User
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment
