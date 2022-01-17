from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'Ajax_test'

urlpatterns =[
    path('list', TemplateView.as_view(template_name='list.html'), name='list'),

    path('get', views.ListJsonAPIView.as_view(), name='getList'),

    #path('edit', ActualWorkFormView.as_view(), name='edit')

    path('show_todo_items', views.show_todo_items, name='show_todo_items'),
    path('create_todo_item/', views.CreateTodoItemFormView.as_view(), name='create_todo_item'),
    path('update_todo_item/<int:pk>', views.UpdateTodoItemFormView.as_view(), name='update_todo_item'),
    path('delete_todo_item/<todo_id>', views.delete_todo_item, name='delete_todo_item'),

    path('create_aw/', views.CreateActualWorkFormView.as_view(), name='create_aw'),
    
]