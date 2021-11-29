from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するcolumnを設定するクラス'''

    #レコード一覧にidとusernameを表示
    list_display = ('id','username')
    #表示するcolumnにリンクを設定
    list_display_links = ('id','username')

# Django管理サイトにCustomUserAdminを登録する
admin.site.register(CustomUser,CustomUserAdmin)

