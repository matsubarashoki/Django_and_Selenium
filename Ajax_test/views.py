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
        newlist = {}
        for x in datalist1:
            newlist['main']= x

            for y in datalist2 :
                #IDが一致するか リストの検索処理をしたいけどindex指定ができぬ
                if x[0] == y[0]:
                    newlist['detail'] = y
        print(newlist)
        

        return JsonResponse(newlist, safe=False)
