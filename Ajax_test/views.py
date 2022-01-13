from django.http.response import JsonResponse
from django.views import generic
from django.db import connection
from rest_framework import generics
from rest_framework.views import APIView
from .models import Matter, ActualWork
from .serializers import ActualWorkSerializer

class ListJsonAPIView(APIView):

    def get(self, request, format=None):
        # 今気づいたけど、直書きSQLの道って果てしなくSQL増えるかな。。いや、何とか頑張ろう
        sql1 = open('Ajax_test\static\sql.txt', 'r',encoding='UTF-8').read()
        sql2 = open('Ajax_test\static\sql2.txt', 'r',encoding='UTF-8').read()
        
        with connection.cursor() as cursor:
            cursor.execute(sql1)
            datalist1 = cursor.fetchall()
            cursor.execute(sql2)
            datalist2 = cursor.fetchall()
        
        #ワンライナーでおしゃれに書きたいけどわからん。。。
        #これdatalist2をはちゃめちゃ回すよな。。絶対よくない。。

        d_keys = [
            "案件ID",
            "稼働ID"
        "担当営業",
        "取引先番号",
        "稼働時間単位",
        "稼働時間",
        "控除or超過時間",
        "基本時間",
        "単価",
        "控除額",
        "超過額",
        "控除or超過実額",
        "特殊品目",
        "特殊品目金額",
        "特殊品目2",
        "特殊品目2金額",
        "支払期日設定",
        "指定振替日設定",
        "支払期日",
        "締め日設定",
        "稼働対象期間",
        "契約期間"]

        newlist = {}
        for index, x in enumerate(datalist1):
            key = "main" + str(index)
            newlist[key]= x
            for index2, y in enumerate(datalist2) :                
                #IDが一致するか リストの検索処理をしたいけどindex指定ができぬ
                if x[0] == y[0] and x[1] == y[1]:
                    key = "detail" + str(index2)
                    #newlist[key] = y
                    d_dic = dict(zip(d_keys,y))
                    newlist[key] = d_dic


        return JsonResponse(newlist, safe=False)
