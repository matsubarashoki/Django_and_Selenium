from django.urls import path

from . import views

app_name = 'makepdf'

urlpatterns = [
    path('', views.pdfIndex, name='pdfIndex'),
     # リクエストされたURLが「blog-detail/レコードID」とマッチしたら、viewsのBlogDetailを実行
]