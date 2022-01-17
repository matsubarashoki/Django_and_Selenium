import imp
from pyexpat.errors import messages
from django import template
from django.forms import BaseModelForm
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
#from django.views import generic
from django.db import connection, models
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.views import APIView
from .models import Matter, ActualWork, TodoItem
from .serializers import ActualWorkSerializer
from .forms import ActualWorkForm, CreateUpdateTodoItemForm
from bootstrap_modal_forms import generic 

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
        
        m_keys=[
            "案件ID",
            "稼働ID",
            "ステータス",
            "社名",
            "案件名",
            "社員名",
            "請求金額",
            "請求日"
        ]
        d_keys = [
            "案件ID",
            "稼働ID",
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
            "契約期間"
            ]
        #ワンライナーでおしゃれに書きたいけどわからん。。。
        #これdatalist2をはちゃめちゃ回すよな。。絶対よくない。。
        newlist = {}
        for index, x in enumerate(datalist1):
            key = "main" + str(index)
            m_dic = dict(zip(m_keys,x))
            newlist[key]= m_dic
            for index2, y in enumerate(datalist2) :                
                #IDが一致するか リストの検索処理をしたいけどindex指定ができぬ
                if x[0] == y[0] and x[1] == y[1]:
                    key = "detail" + str(index2)
                    #newlist[key] = y
                    d_dic = dict(zip(d_keys,y))
                    newlist[key] = d_dic


        return JsonResponse(newlist, safe=False)

# class ActualWorkFormView(generic.FormView):
#     template_name = 'list.html'
#     form_class = ActualWorkForm


#Modal処理サンプル
def show_todo_items(request):
    all_items = TodoItem.objects.filter(user=request.user)
    return render(request, 'show_todo_items.html',{'all_items': all_items})

class CreateTodoItemFormView(generic.BSModalCreateView):
    template_name = 'create_modal_form.html'
    form_class = CreateUpdateTodoItemForm
    success_message = '成功しました'
    success_url = reverse_lazy('Ajax_test:show_todo_items')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class UpdateTodoItemFormView(generic.BSModalUpdateView):
    model = TodoItem
    template_name = 'update_modal_form.html'
    form_class = CreateUpdateTodoItemForm
    success_message = '更新しました'
    success_url = reverse_lazy('Ajax_test:show_todo_items')

def delete_todo_item(request, todo_id):
    item = TodoItem.objects.get(pk=todo_id)
    item.delete()
    messages.success = (request, ('削除しました'))
    return redirect('Ajax_test:show_todo_items')


#Modal処理　ActualWork
class CreateActualWorkFormView(generic.BSModalCreateView):
    template_name = 'create_modal_form.html'
    form_class = ActualWorkForm
    success_message = '成功しました'
    success_url = reverse_lazy('Ajax_test:show_todo_items')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)
