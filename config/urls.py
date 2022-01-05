
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #youtube_textアプリへのURLパターンを追加
    path('',include('youtube_text.urls')),
    #アカウントアプリのURLパターンを追加
    path('',include('user_setting.urls')),
    #blogのURLパターンを追加
    path('',include('blog.urls')),
    #allauthのURL
    # path('accounts/',include('allauth.urls')),

    #PDF作成
    path('makepdf/',include('makepdf.urls')),

]
