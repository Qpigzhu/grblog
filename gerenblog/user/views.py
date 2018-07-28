from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.contrib import auth
from django.views import View
from django.http import HttpResponseRedirect
#加密密码
from django.contrib.auth.hashers import make_password
# Create your views here.

from .forms import LoginForm,ReForm,ForgetpwdForm,ForgetForm
from user.models import UserProfile,EmailVerifRecord

from .email_send import send_email
#并集查询
from django.db.models import Q


#重写登录验证方法,使得可以使用邮箱登录
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


#激活用户
class ActiveUserView(View):
    def get(self,request,active_code):
        # 查询邮箱验证是否存在记录
        all_record = EmailVerifRecord.objects.filter(code=active_code)
        if all_record:
            for record in all_record:
                #找到对应的邮箱
                email = record.email
                #用邮箱查找用户
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                EmailVerifRecord.objects.filter(email=email).delete()
                return render(request,'lw-log.html')
        else:
            return render(request, 'lw-re.html',{'msg':'链接失效'})


#登录
class LoginView(View):
    def get(self,request):
        #获取请求登录的页面
        from_s = request.GET.get('from', '')
        return render(request,'lw-log.html',{"from_s":from_s})

    def post(self,request):
        login_form = LoginForm(request.POST)
        #验证是否通过表单
        if login_form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')


            # 验证用户是否匹配，匹配成功返回user对象，否则为空
            user = authenticate(username=username,password=password)
            if user is not None:
                #查看用户是否激活
                if user.is_active:
                    auth.login(request,user)
                    #返回首页
                    return redirect(request.POST.get('next',reverse('home')))
                else:
                    return render(request,'lw-log.html',{"msg":"用户未激活"})
            else:
                return render(request, 'lw-log.html', {"msg": "用户或密码错误"})
        else:
            return render(request,'lw-log.html',{"login_form":login_form})

#退出登录
class OutLoginView(View):
    def get(self,request):
        auth.logout(request)
        return redirect(request.GET.get('from', reverse('home')))

#注册账号
class ReUserView(View):
    def get(self,request):
        re_form = ReForm()
        return render(request,'lw-re.html',{'re_form':re_form})
    def post(self,request):
        re_form = ReForm(request.POST)
        #验证是否通过
        if re_form.is_valid():
            email = request.POST.get('email','')
            password = request.POST.get('password','')

            #判断是否相同邮箱
            emails = UserProfile.objects.filter(email=email)
            if emails:
                return render(request, 'lw-re.html', {'re_form': re_form, 'msg': '邮箱已经被注册'})
            else:
                add_user = UserProfile()
                add_user.username = email
                add_user.email = email
                add_user.is_active = False
                # 加密密码进行保存
                add_user.password = make_password(password)
                add_user.save()

                #发激活邮件给用户
                send_email(email,'register')
                return render(request,'lw-log.html',{'msg':'激活邮件已发送'})
        else:
            return render(request, 'lw-re.html', {'re_form': re_form})


#发送重置密码邮件
class ForgetPwdView(View):
    def get(self,request):
        forget_from = ForgetpwdForm()
        return render(request,'forget.html',{'forget_from':forget_from})
    def post(self,request):
        forget_from = ForgetpwdForm(request.POST)
        if forget_from.is_valid():
            email = request.POST.get('email','')
            if UserProfile.objects.filter(email=email):
                send_email(email,'forget')
                return render(request,'lw-log.html',{'msg':"邮箱已发送成功"})
            else:
                return render(request,'forget.html',{'forget_from':forget_from,'user_msg':'用户不存在'})
        else:
            return render(request,'forget.html',{'forget_from':forget_from})

#返回重置密码页面
class ForgetHtmlView(View):
    def get(self,request,forget_code):
        all_record = EmailVerifRecord.objects.filter(code=forget_code,send_type='forget')
        if all_record:
            for record in all_record:
                email = record.email
            return render(request,'forget_pwd.html',{'email':email})
        else:
            return render(request,'forget.html',{'msg':"链接失效"})


class ForgetPwdDatilView(View):
    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email','')
            pwd1 =request.POST.get('pwd1','')
            pwd2 =request.POST.get('pwd2','')
            if pwd1 != pwd2:
                return render(request,'msg.html', {'msg':'密码不一致'})

            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            EmailVerifRecord.objects.filter(email=email).delete()
            return render(request,'lw-log.html',{'msg':'密码已重置'})
        else:
            return render(request,'msg.html',{'msg':'密码不一致'})
