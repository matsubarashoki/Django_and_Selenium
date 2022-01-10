from django.http.response import JsonResponse
from django.views import generic
from django.db import connection
from rest_framework import generics
from rest_framework.views import APIView
from .models import Matter, ActualWork
from .serializers import ActualWorkSerializer

class ListJsonAPIView(APIView):

    def get(self, request, format=None):
        sql = open('Ajax_test\static\sql.txt', 'r',encoding='UTF-8').read()
        print(type(sql))
        with connection.cursor() as cursor:
            cursor.execute(sql)
            datalist = cursor.fetchall()
        return JsonResponse(datalist, safe=False)
