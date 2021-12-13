# Django_and_Selenium
ポートフォリオ用サイト
PythonのDjangoを活用したWEBアプリです。

# Features
・
Django.core.exceptions によるvalidation

# Requirement
主なものだけ記載（詳細はrequirementをご確認ください）
Python==3.7.11
Django==2.2.5
django-environ==0.8.1(環境変数用)
django-glrm==1.1.3(ログイン必須処理)
newsapi-python==0.2.6(ニュース一覧用 APIKeyはご自身で取得してください)
psycopg2==2.8.6(DB用)
selenium==4.1.0(スクレイピング用)
chromedriver-binary==96.0.4664.45.0

# NewsAPI


# Usage
#クローンして実行するための手順
pip install ~~と

.envの作成

postgresqlでテーブル作成
以下コマンド


python manage.py runserver



# Note
とても汚いコードとコメントが残っています。
なるべく早く修正していきます。。。
本アプリによる
