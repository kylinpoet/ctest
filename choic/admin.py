from django.contrib import admin
from .models import *



# Register your models here.

class ChoicesAdmin(admin.ModelAdmin):
    list_display = ('body','bodyselect','bssort','rightanswer')
    list_per_page = 100
    ordering = ('-bodyselect','bssort',)
    list_editable = ['bodyselect','bssort']

    # 筛选器
    list_filter = ('bodyselect','bssort',)  # 过滤器
    search_fields = ( 'body',)  # 搜索字段
    date_hierarchy = 'creattime'  # 详细时间分层筛选


class CresultAdmin(admin.ModelAdmin):
    list_display = ('question','user','studentname','answerstate','answer','correct','answertime')
    list_filter = ('question', 'user',)  # 过滤器
    date_hierarchy = 'answertime'
    def studentname(self,obj):
        return obj.user.first_name
    def correct(self,obj):
        return obj.question.rightanswer
admin.site.register(Tag)
admin.site.register(Cresult,CresultAdmin)
admin.site.register(Choices,ChoicesAdmin)

admin.AdminSite.site_header = '选题系统管理后台Q1074373176Q'
admin.AdminSite.site_title = '选题系统'