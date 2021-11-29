from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog', views.BlogView.as_view(), name='blog'),
     # リクエストされたURLが「blog-detail/レコードID」とマッチしたら、viewsのBlogDetailを実行
    path('blog-detail/<int:pk>/', views.BlogArticle.as_view(), name='blog_detail'),   

    path('inquiry', views.InquiryView.as_view(), name='inquiry'),
]