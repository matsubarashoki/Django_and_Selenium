# Django_and_Selenium
ポートフォリオ用サイト
PythonのDjangoを活用したWEBアプリです。
デモサイト：http://matsukari.pythonanywhere.com/

# 主な機能
・管理者によるブログ記事作成機能
・記事へのコメント追加機能
・問い合わせ機能（メール送信）
・ニュースAPIによるニュース一覧
・スクレイビングによる動画文字起こし取得＆履歴管理

# Features
・Djangoの汎用クラスビューでCRUD機能を1クラスに集約（
・Django fixtureによる初期設定データ投入
・Django.core.exceptions によるvalidation（動画リンクのURL指定

# Requirement
主なものだけ記載（詳細はrequirementをご確認ください）
・Python==3.7.11\n
・Django==2.2.5
・django-environ==0.8.1(環境変数用)
・django-glrm==1.1.3(ログイン必須処理)
・newsapi-python==0.2.6(ニュース一覧用 APIKeyはご自身で取得してください)
・psycopg2==2.8.6(DB用)
・selenium==4.1.0(スクレイピング用)
・chromedriver-binary==96.0.4664.45.0

# NewsAPI


# Usage
#クローンして実行するための手順
pip install -r requirement.txt

.envの作成

postgresqlでテーブル作成
以下コマンド

python manage.py createsuperuser
ユーザー名: admin
メールアドレス:

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata blog/fixtures/initial_data.json

python manage.py runserver

作成したスーパーユーザでログイン
http://127.0.0.1:8000/login

# Note
とても汚いコードとコメントが残っています。
なるべく早く修正していきます。。。
本アプリによる
