from django.urls import path
from django.views.generic.base import TemplateView

from .views import ListJsonAPIView,ActualWorkFormView

app_name = 'Ajax_test'

urlpatterns =[
    path('list', TemplateView.as_view(template_name='list.html'), name='list'),

    path('get', ListJsonAPIView.as_view(), name='getList'),

    path('edit', ActualWorkFormView.as_view(), name='edit')
]