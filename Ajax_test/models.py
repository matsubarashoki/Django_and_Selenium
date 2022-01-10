from re import T
from django.db import models
from django.core import validators
from user_setting.models import CustomUser


class Matter(models.Model):

    """
    Matterテーブル
        ID:独自にしようか迷ったけどやめとく
        担当営業
        ステータス
        取引先番号
        社名
        案件名
        基本時間
        支払期日設定
        指定振替日
        締め日
        期間
        登録日
        登録ユーザ
        ※長いから技術系はまた今度
    """
    tantou_sales = models.CharField(
        verbose_name='担当営業',
        max_length=20,
    )

    STATUS_CHOICES = (
        (1, '稼働中'),
        (2, '終了'),
    )
    status = models.SmallIntegerField(
        verbose_name='ステータス',
        choices=STATUS_CHOICES,
        default=1
    )

    client_number = models.SmallIntegerField(
        verbose_name='取引先番号',
    )

    company_name = models.CharField(
        verbose_name='社名',
        max_length=50,
    )

    matter_name = models.CharField(
        verbose_name='案件名',
        max_length=50,
    )

    base_time  = models.CharField(
        verbose_name='基本時間',
        max_length=50,
    )  

    pay_date_choices = (
        (1,'翌月25日'),
        (2,'翌月末'),
        (3,'翌々月5日'),
        (4,'翌々月10日'),
        (5,'翌々月15日'),
        (6,'翌々月20日'),
        (7,'翌々月25日'),
        (8,'翌々月末'),
        (9,'その他'),
    )
    payment_date_settting = models.SmallIntegerField(
        verbose_name='支払期日設定',
        choices=pay_date_choices,
        default=1
    )

    transfer_date_choices = (
        (1,'直前営業日'),
        (2,'翌営業日'),
        (3,'その他'),
    )   
    Transfer_date =  models.SmallIntegerField(
        verbose_name='指定振替日設定',
        choices=transfer_date_choices,
        default=1
    )

    closing_date_choices = (
        (1,'月末'),
        (2,'15日'),
        (3,'20日'),
    )   
    closing_date = models.SmallIntegerField(
        verbose_name= '締め日設定',
        choices=closing_date_choices,
        default=1
    )

    delete_flg = models.IntegerField(
        verbose_name='削除フラグ',   
    )

    create_user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='登録ユーザ',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.DO_NOTHING
    )

    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.matter_name

    class Meta:
        verbose_name = '案件'

class ActualWork(models.Model):

    """
    ActualWork(稼働)テーブル
        ID
        外部キー
        社員No
        社員名
        稼働時間単位
        稼働時間（h）
        控除or超過時間
        単価
        控除金額
        超過金額
        控除or超過金額
        特殊品目
        特殊品目金額
        特殊品目２
        特殊品目金額２
        請求金額
        請求日
        支払い期日
        稼働対象期間
        契約期間
        登録日
        登録ユーザ
        更新日
        更新ユーザ
    """

    matter_id = models.ForeignKey(
        Matter,
        verbose_name='案件ID',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
    )

    emp_num = models.CharField(
        verbose_name='社員番号',
        max_length=20
    )

    emp_name = models.CharField(
        verbose_name='社員名',
        max_length=20
    )

    actual_time_unit = models.SmallIntegerField(
        verbose_name='稼働時間単位',
    )

    actual_time = models.DecimalField(
        verbose_name='稼働時間',
        max_digits=5,
        decimal_places=2,
    )

    over_time = models.DecimalField(
        verbose_name='控除or超過時間',
        max_digits=3,
        decimal_places=2,
    )

    payment = models.IntegerField(
        verbose_name='単価'
    )

    deducting = models.SmallIntegerField(
        verbose_name='控除額'
    )

    excess = models.SmallIntegerField(
        verbose_name='超過額'
    )

    over_amount = models.IntegerField(
        verbose_name='控除or超過金額'
    )

    s_item_choices = (
        (1,'出張交通費(税込)'),
        (2,'出張交通費(税込)'),
        (3,'出張交通費(税抜)'),
        (4,'出張日当-宿泊費(税込)'),
        (5,'出張日当-宿泊費(税抜)'),
        (6,'立替交通費(税込)'),
        (7,'立替交通費(税抜)'),
        (8,'その他(税込)'),
        (9,'その他(税抜)'),
    )   

    special_item1 = models.SmallIntegerField(
        verbose_name='特殊品目',
        choices=s_item_choices,
        blank=True,null=True,
    )
    special_item1_amount = models.IntegerField(
        verbose_name='特殊品目金額',
        blank=True,null=True,
    )

    special_item2 = models.SmallIntegerField(
        verbose_name='特殊品目2',
        choices=s_item_choices,
        blank=True,null=True,

    )
    special_item2_amount = models.IntegerField(
        verbose_name='特殊品目2金額',
        blank=True,null=True,
    )

    total_amount = models.IntegerField(
        verbose_name='請求金額'
    )

    billing_date = models.DateField(
        verbose_name='請求日'
    )

    deadline = models.DateField(
        verbose_name='支払期日'
    )

    work_duration = models.CharField(
        verbose_name='稼働対象期間',
        blank=True,null=True,
        max_length=90
    )

    contract_duration = models.CharField(
        verbose_name='契約期間',
        blank=True,null=True,
        max_length=90,
    )

    # actual_period = models.DurationField(
    #     verbose_name='稼働対象期間',
    #     blank=True,null=True
    # )

    # contract_period = models.DurationField(
    #     verbose_name='契約期間',
    #     blank=True,null=True,
    # )

    aw_create_user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='AW登録ユーザ',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.DO_NOTHING
    )

    aw_created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.emp_name 

    class Meta:
        verbose_name = '稼働'
