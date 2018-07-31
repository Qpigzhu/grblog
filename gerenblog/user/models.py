from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey




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

#点赞数量
class LikeNumber(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','content_object')
    likes_num = models.IntegerField(default=0)

    class Meta:
        verbose_name = "点赞数量"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}:{}:{}'.format(self.content_type,self.object_id,self.likes_num)


#点赞的用户
class LikeDatil(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    like_time = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','content_object')

    class Meta:
        verbose_name = "具体点赞详情"

    def __str__(self):
        return '{}:{}:{}'.format(self.user,self.content_type, self.object_id)


#收藏
class House_Blog(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,default='')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','content_object')

    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户",default='')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"评论时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.user,self.object_id)