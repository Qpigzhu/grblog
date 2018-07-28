from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



#用户信息
class UserProfile(AbstractUser):
    nice_name = models.CharField(max_length=50,verbose_name="昵称",default="")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female",verbose_name="性别")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image  = models.ImageField(upload_to="author/%Y/%m",default="")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

#邮箱验证码
class EmailVerifRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name="邮箱")
    send_type = models.CharField(max_length=10,choices=(("register",u"注册"),("forget",u"忘记密码")),verbose_name="注册类型")
    send_time = models.DateTimeField(auto_now_add=True,verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}{}'.format(self.email,self.code)

