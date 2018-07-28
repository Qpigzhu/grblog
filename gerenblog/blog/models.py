from django.db import models
from user.models import UserProfile

# Create your models here.



class BlogType(models.Model):
    type_name = models.CharField(max_length=10)

    class Meta:
        verbose_name = "文章类型"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.type_name




class Blog(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题")
    type_name = models.ForeignKey(BlogType,on_delete=models.CASCADE,verbose_name="文章类型")
    content = models.TextField(verbose_name="文章内容")
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    read_datails = models.IntegerField(default=0,verbose_name="阅读数量")
    images = models.ImageField(upload_to="blog/%Y/%m",default="",max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "博客具体信息"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
