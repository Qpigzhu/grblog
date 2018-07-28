# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\7\26 0026 18:21$'

import xadmin
from xadmin import views
from .models import Blog,BlogType


# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "个人博客后台管理"
    site_footer = "Pig博客"
    #收起菜单
    menu_style = "accordion"


class BlogAdmin(object):
    list_display = ['title','type_name','author','read_datails','created_time','last_update_time']
    search_fields = ['title','type_name','author']
    list_filter = ['title','type_name','author','created_time','last_update_time']
xadmin.site.register(Blog, BlogAdmin)

class BlogTypeAdmin(object):
    list_display = ['id', 'type_name']
    search_fields = ['id', 'type_name']
    list_filter = ['id', 'type_name']
xadmin.site.register(BlogType, BlogTypeAdmin)


# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView,GlobalSettings)