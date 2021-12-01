import datetime
import os
import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import SearchLog

class Command(BaseCommand):
    #コマンドの属性を記述
    help = "Backup　SearchLog"

    #BaseCommandのhandleをオーバーライド
    def handle(self, *args, **kwargs):
        #実行日取得
        date = datetime.date.today().strftime("%Y%m%d")

        #保存ファイルの相対パス
        file_path = str(settings.BACKUP_PATH) + 'SerchLog_' + date + '.csv'
        print(file_path)

        #　保存ディレクトリが存在しなければ作成
        os.makedirs(settings.BACKUP_PATH, exist_ok=True)

        #バックアップファイル作成
        with open(file_path, 'w') as file:
            writer = csv.writer(file)

            #ヘッダーの書き込み
            header = [field.name for field in SearchLog._meta.fields]
            writer.writerow(header)

            #SearchLogテーブルの全データ取得
            SearchLogs = SearchLog.objects.all()

            #データ書き込み
            for Log in SearchLogs:
                writer.writerow([
                    str(Log.user),
                    Log.title,
                    Log.url,
                    Log.result,
                    str(Log.search_date),
                ])

        #保存ディレクトリのファイルリストを取得
        files = os.listdir(settings.BACKUP_PATH)
        #ファイルが設定数以上あれば一番古いファイルを削除
        if len(files) >= settings.NUM_SAVED_BACKUP:
            files.sort()
            os.remove(settings.BACKUP_PATH + files[0])