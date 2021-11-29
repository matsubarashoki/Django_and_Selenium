from django.db import models
from user_setting.models import CustomUser
from .validator import validate_url

class SearchLog(models.Model):
    ''' 実行履歴モデル'''
    # 動画タイトル用のフィールド　スクレイピング中に取得
    title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=200,        # 最大文字数は200
        default="動画タイトル"
        )
    #User
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )

    #検索したURL
    url = models.CharField(
        verbose_name='URL',
        max_length=500,
        validators=[validate_url]
    )
    #結果
    result = models.CharField(
        verbose_name='結果',
        max_length=100,
        default="未実施"
    )
    #実行日
    search_date = models.DateTimeField(
        verbose_name="検索日時",
        auto_now_add=True
    )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す'''
        return self.url