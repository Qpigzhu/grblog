"""gerenblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from .settings import MEDIA_ROOT
from django.views.static import serve
from blog.views import Blog_list_View
from user.views import LoginView,OutLoginView,ReUserView,ActiveUserView,ForgetPwdView,ForgetHtmlView,ForgetPwdDatilView

import xadmin
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',Blog_list_View.as_view(),name="home"),
    path('blog/',include("blog.urls")),
    path('login/',LoginView.as_view(),name="login"),
    path('outlogin/',OutLoginView.as_view(),name="out_login"),
    path('re/',ReUserView.as_view(),name="re_user"),
    #发送重置密码url
    path('forget/',ForgetPwdView.as_view(),name="forget"),
    #重置密码链接URL
    re_path('forget/(?P<forget_code>.*)/',ForgetHtmlView.as_view(),name='forget_html'),
    #处理重置密码URL
    path('forgetpwd/',ForgetPwdDatilView.as_view(),name='forget_pwd'),
    #激活url
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='active_user'),

# 验证码url
    path("captcha/", include('captcha.urls')),
    #图片上传url处理
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

]
