# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\7\27 0027 21:46$'

from django import forms
from user.models import UserProfile
# 引入验证码field
from captcha.fields import CaptchaField

#登录表单
class LoginForm(forms.Form):
    username = forms.CharField(required=True,error_messages={'required':u'用户名不能为空'})
    password = forms.CharField(required=True,error_messages={'required':u'密码不能为空'})

#注册表单
class ReForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    # 应用验证码
    captcha = CaptchaField(required=True,error_messages={"invalid":"验证码错误","required":u"请输入验证码"})

#发送重置密码邮件表单
class ForgetpwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})

#重置密码表单
class ForgetForm(forms.Form):
    pwd1 = forms.CharField(required=True,min_length=5)
    pwd2 = forms.CharField(required=True,min_length=5)
