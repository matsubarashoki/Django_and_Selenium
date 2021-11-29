from django.urls import path
from .import views

app_name = 'youtube_text'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # Log_list
    path('log_list/',views.LogListView.as_view(),name = 'log_list'),

    #　Detail
    path('detail/<int:pk>',views.DetailView.as_view(),name = 'detail'),

    # スクレイピングviewsモジュールのCrを実行
    path('scraping/', views.Scraping.as_view(), name='scraping'),

    # news_list
    path('news/',views.NewsListView.as_view(),name = 'news_list'),

    # result
    path('result/',views.ResultView.as_view(),name = 'result'),
]