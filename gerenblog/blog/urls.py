# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\7\25 0025 19:11$'

from django.urls import path
from .views import Blog_list_View,blog_datail_View,BlogTypeView

urlpatterns = [
    path('<int:blog_pk>',blog_datail_View.as_view(),name="blog_datail"),
    path('type/<int:type_pk>',BlogTypeView.as_view(),name="blog_type"),

]