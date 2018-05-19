from django.shortcuts import render,redirect,HttpResponse,render_to_response,HttpResponseRedirect
from reg.models import *
from goods.models import *
from datetime import datetime
import hashlib
from comments.filter_user import filt
import json
# Create your views here.
def register(request):
    if request.method == "POST":
        post = request.POST
        user_name = post.get('user_name','')
        pwd = post.get('pwd','')
        cpwd = post.get('cpwd','')
        email = post.get('email','')
        # 判断两次密码是否相等

        #加密密码
        md = hashlib.md5()
        md.update(pwd.encode())
        pwd = md.hexdigest()
        # 生成时间戳
        #int(time.time())
        User.objects.create(**{'uname':user_name,'upassword':pwd,'uemail':email,'uregister_time':datetime.now()})
        rep = HttpResponseRedirect('/reg/login/')
        rep.set_cookie('uname',user_name)
        return rep
    return render(request,'reg/register.html',{'title':'注册'})

def user_is_exists(request):
    name = request.GET.get('name')
    # user_exist = json.dumps(User.objects.filter(uname=name).count())
    user_exist = User.objects.filter(uname=name).count()
    print(type(user_exist))
    return HttpResponse(user_exist)
    # return HttpResponse("ok")
def login(request):
    uname = request.COOKIES.get('uname','')

    if request.method == "POST":
        post = request.POST
        username = post.get("username","")
        pwd = post.get("pwd",'')
        ge = post.get("ge",0)
        # 比较密码
        md = hashlib.md5()
        md.update(pwd.encode())
        h_pwd = md.hexdigest()

        users = User.objects.filter(uname=username,upassword=h_pwd)
        if users:
            urlpath = request.COOKIES.get("url","/")
            re = HttpResponseRedirect(urlpath)
            if int(ge) == 1:
                re.set_cookie('uname',username)
            else:
                re.set_cookie('uname','',max_age=-1)
            request.session['uid'] = users[0].id
            request.session['uname'] = username
            return re
        else:
             # 记录用户信息
            user_context = {'title':'用户登录','error':'用户名或密码错误','uname':uname,'upwd':pwd}
            return render(request,'reg/login.html',user_context)
    user_context = {'title':'用户登录','error':None,'uname':uname}
    return render(request,'reg/login.html',user_context)

@filt
def userinfo(request):
    goods_id = request.COOKIES.get("gids",'')
    uid = request.session.get("uid")
    try:
        goods_id = goods_id.split(",")
        goods_data = []
        for gid in goods_id:
            goods_data.append(goods.objects.get(id=gid))
    except:
        return render(request,'reg/user_center_info.html',{'goods_data':goods_data})

    uu = User.objects.get(id=uid)

    return render(request,'reg/user_center_info.html',{'goods_data':goods_data,'uu':uu})
def logout(request):
    request.session.flush()
    return redirect('/')

@filt
def addaddress(request):
    uid = request.session.get("uid")
    if request.method == "POST":
        usname = request.POST.get("usname",'')
        uphone = request.POST.get("uphone",'')
        uaddress = request.POST.get('uaddress','')

    User.objects.filter(id=uid).update(usname=usname,uphone=uphone,uaddress=uaddress)
    return redirect("/reg/userinfo/")
