# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\7\28 0028 11:27$'
"""
    发邮件
"""
from random import Random
from user.models import EmailVerifRecord
# 导入Django自带的邮件模块
from django.core.mail import send_mail
#导入设置邮箱信息
from gerenblog.settings import EMAIL_FROM

#生成随机字符串
def random_str(random_length = 8):
    str = ''
    #生成可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0,length)]
    return str


def send_email(email,send_type='register'):
    #实例化邮箱验证对象
    code = random_str(16)
    email_record = EmailVerifRecord()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    #定义邮件内容和标题
    email_title = ""
    email_content = ""

    #判断邮件是否注册类型
    if send_type == 'register':
        email_title = 'Pig博客网站 注册激活链接'
        email_content = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/active/{0}".format(code)

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，从哪里发，接受者list,成功返回1
        send_status = send_mail(email_title,email_content,EMAIL_FROM,[email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = 'Pig博客网站 重置密码链接'
        email_content = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/forget/{0}".format(code)

        send_status = send_mail(email_title,email_content,EMAIL_FROM,[email])
        if send_status:
            pass
