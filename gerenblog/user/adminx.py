# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\7\27 0027 20:38$'

import xadmin
from .models import EmailVerifRecord


class EmailVerifRecordAdmin(object):
    list_dispy = ['code','email','send_type','send_time']
    search_fields = ['email','send_type']
    list_filter = ['email','send_type']
xadmin.site.register(EmailVerifRecord,EmailVerifRecordAdmin)