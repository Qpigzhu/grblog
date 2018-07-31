# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\7\27 0027 20:38$'

import xadmin
from .models import EmailVerifRecord,LikeNumber,LikeDatil,House_Blog


class EmailVerifRecordAdmin(object):
    list_dispy = ['code','email','send_type','send_time']
    search_fields = ['email','send_type']
    list_filter = ['email','send_type']
xadmin.site.register(EmailVerifRecord,EmailVerifRecordAdmin)


class LikeNumberAdmin(object):
    list_dispy = ['content_type','object_id','likes_num']
    search_fields = ['content_type','object_id','likes_num']
    list_filter = ['content_type','object_id','likes_num']
xadmin.site.register(LikeNumber,LikeNumberAdmin)

class LikeDatilAdmin(object):
    list_dispy = ['content_type','object_id','user']
    search_fields = ['content_type','object_id','user']
    list_filter = ['content_type','object_id','user']
xadmin.site.register(LikeDatil,LikeDatilAdmin)

class HouseAdmin(object):
    list_dispy = ['user','content_type', 'object_id','add_time']
    search_fields = ['user','content_type', 'object_id']
    list_filter = ['user','content_type', 'object_id']

xadmin.site.register(House_Blog,HouseAdmin)