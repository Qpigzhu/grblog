from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Blog,BlogType
from django.contrib.contenttypes.models import ContentType
from user.models import LikeDatil,LikeNumber,House_Blog
# Create your views here.
#分页功能
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


#Blog列表
class Blog_list_View(View):
    def get(self,request):
        blog_list_all = Blog.objects.all()
        all_blog_type = BlogType.objects.all()

        #分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(blog_list_all, 5, request=request)
        blog_list = p.page(page)


        return render(request,"index.html",{
            "blog_list":blog_list,
            "all_blog_type":all_blog_type,
        })

#文章详情页
class blog_datail_View(View):
    def get(self,request,blog_pk):
        blog_datail = get_object_or_404(Blog,pk = blog_pk)
        all_blog_type = BlogType.objects.all()

        #上一篇博客
        previous_blog = Blog.objects.filter(created_time__gt=blog_datail.created_time).last()
        #下一遍博客
        next_blog = Blog.objects.filter(created_time__lt=blog_datail.created_time).first()

        #判断用户是否已经点赞
        active_like = ''
        content_type = ContentType.objects.get_for_model(Blog)
        #判断是否登录
        if request.user.is_authenticated:
            #判断是否存在点赞记录
            if LikeDatil.objects.filter(content_type=content_type,object_id=blog_pk,user=request.user):
                active_like = 'am-icon-heart'
            else:
                active_like = 'am-icon-heart-o'
        else:
            active_like='am-icon-heart-o'
        #获取点赞总数
        try:
            like_number = LikeNumber.objects.get(content_type=content_type,object_id=blog_pk).likes_num
        except:
            like_number = 0

        #判断用户是否已经收藏
        if request.user.is_authenticated:
            if House_Blog.objects.filter(user=request.user,content_type=content_type,object_id=blog_pk):
                active_house = 'am-icon-star'
            else:
                active_house = 'am-icon-star-o'
        else:
            active_house = 'am-icon-star-o'



        return render(request,"blog_datil.html",{
            "blog":blog_datail,
            "all_blog_type": all_blog_type,
            "previous_blog":previous_blog,
            "next_blog":next_blog,
            "active_like":active_like,
            'like_number':like_number,
            "active_house": active_house,
        })

#Blog类型处理
class BlogTypeView(View):
    def get(self,request,type_pk):
        type_id = get_object_or_404(BlogType,id = type_pk)
        all_blog_type = BlogType.objects.all()
        all_type_blog = Blog.objects.filter(type_name=type_id)

        #分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_type_blog, 5, request=request)
        type_blog = p.page(page)

        return render(request,"blog_type.html",{
            "type_name":type_id,
            "blog_type":type_blog,
            "all_blog_type": all_blog_type,
        })