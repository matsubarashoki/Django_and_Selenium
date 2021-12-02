from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog', views.BlogView.as_view(), name='blog'),
     # リクエストされたURLが「blog-detail/レコードID」とマッチしたら、viewsのBlogDetailを実行
    path('blog-detail/<int:pk>/', views.BlogArticle.as_view(), name='blog_detail'),   

    #path('comment_update/<int:b_id>/<int:c_id>/', views.CommentUpdate, name='comment_update'),   
    # PK複数の時はオブジェクトも指定する
    path('comment-delete/<int:comment_blogpost_pk>/<int:comment_pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),   

    path('inquiry', views.InquiryView.as_view(), name='inquiry'),
]