#coding:utf-8
from django.shortcuts import render
from goods.models import  *
from django.db.models import F
from django.core.paginator import Paginator
from cart.models import *
# Create your views here.

def index(request):
    # 每个分类 4个最热的，4个最新的
    type_list = gtype.objects.all()
    type0 = type_list[0].goods_set.order_by('-id')[0:4]
    type01 = type_list[0].goods_set.order_by('-gclick')[0:4]
    type1 = type_list[1].goods_set.order_by('-id')[0:4]
    type11 = type_list[1].goods_set.order_by('-gclick')[0:4]
    type2 = type_list[2].goods_set.order_by('-id')[0:4]
    type21 = type_list[2].goods_set.order_by('-gclick')[0:4]
    type3 = type_list[3].goods_set.order_by('-id')[0:4]
    type31 = type_list[3].goods_set.order_by('-gclick')[0:4]
    type4 = type_list[4].goods_set.order_by('-id')[0:4]
    type41 = type_list[4].goods_set.order_by('-gclick')[0:4]
    type5 = type_list[5].goods_set.order_by('-id')[0:4]
    type51 = type_list[5].goods_set.order_by('-gclick')[0:4]
    uname = request.COOKIES.get('uname')
    uid = request.session.get("uid")
    uu = carttable.objects.filter(uid=uid).count()
    context = {'title':'首页','guest_cart':1,'type0':type0,'type01':type01,
               'type1':type1,'type11':type11,'type2':type2,'type21':type21,
               'type3':type3,'type31':type31,'type4':type4,'type41':type41,
               'type5':type5,'type51':type51,'uname':uname,'uu':uu
               }
    return render(request,'goods/index.html',context)

def detail(request,id):
    uid = request.session.get("uid")
    uu = carttable.objects.filter(uid=uid).count()
    return render(request,'goods/detail.html',{'uu':uu})

def list(request,type,page,sort):
    uid = request.session.get("uid")
    uu = carttable.objects.filter(uid=uid).count()
    # get new
    new = gtype.objects.get(id=type).goods_set.order_by("-id")[0:2]
    letype = gtype.objects.get(id=type)
    # get info
    info = ''
    sort = int(sort)
    if sort == 1:
        info = gtype.objects.get(id=type).goods_set.order_by("-id")
    elif sort == 2:
        info = gtype.objects.get(id=type).goods_set.order_by("-gprice")
    elif sort == 3:
        info = gtype.objects.get(id=type).goods_set.order_by("-gclick")
    paginator = Paginator(info,10)
    page = paginator.page(int(page))
    context = {'new':new,'type':type,'page':page,'sort':sort,'paginator':paginator,'uu':uu,'letype':letype}
    return render(request,'goods/list.html',context)




def goods_info(request,gc,gid):
    uid = request.session.get("uid")
    uu = carttable.objects.filter(uid=uid).count()
    uname = request.COOKIES.get('uname')
    goods_new = gtype.objects.get(id=gc).goods_set.order_by("-id")[0:2]
    goods.objects.filter(id=gid).update(gclick=F('gclick')+1)
    ginfo = goods.objects.get(id=gid)
    context = {'goods_new':goods_new,'ginfo':ginfo,'type':gc,'uname':uname,'uu':uu}
    response =  render(request,'goods/detail.html',context)
    goods_ids = request.COOKIES.get('gids','')
    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')
        if goods_ids1.count(gid)>=1:
            goods_ids1.remove(gid)
        goods_ids1.insert(0,gid)
        if len(goods_ids1) > 6:
            del goods_ids1[5]
        goods_ids1 = ",".join(goods_ids1)
        response.set_cookie('gids',goods_ids1)
    else:
        goods_ids = gid
        response.set_cookie('gids',goods_ids)

    return response








