from django.shortcuts import render,HttpResponse,redirect
from cart.models import  *
from django.db import transaction
from order.models import *
import datetime
from reg.models import *
from django.http import JsonResponse
from comments.filter_user import filt
import json
# Create your views here.

def orderinfod(request):
    uid = request.session.get("uid")
    cartids = request.GET.getlist('cartid')
    cartids1 = [ int(item) for item in cartids]
    carts = carttable.objects.filter(gid__in=cartids1,uid=request.session.get('uid'))
    uu = User.objects.get(id=uid)
    context = {'title':'提交订单','carts':carts,'cartids':",".join(cartids),'uu':uu}

    return render(request,'order/place_order.html',context)
@filt
@transaction.atomic()
def orderheader(request):
    tran_id = transaction.savepoint()
    cart_ids = request.POST.get('cart_ids')
    try:
        order = OrderInfo()
        now = datetime.datetime.now()
        uid = request.session.get('uid')
        order.oid = "%s%d" % (now.strftime("%Y%m%d%H%M%S"),uid)
        order.user_id = uid
        order.odate = now
        order.total = request.POST.get('total')
        order.save()
    # 创建详单对象
        cart_ids1 = [int(item) for item in cart_ids.split(',')]
        for id1 in cart_ids1:
                detail = Orderdetailinfo()
                # cart = carttable.objects.filter(gid=id1,uid=request.session.get('uid'))
                cart = carttable.objects.get(gid=id1,uid=uid)
                detail.gid_id = id1
                detail.count = cart.count
                detail.price = cart.gid.gprice
                detail.orid = order
                detail.save()
                cart.delete()
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print(e.args)
        transaction.savepoint_rollback(tran_id)
    return redirect('/order/orderlist/')


@filt
def orderlist(request):
    # 先拿用户id，拿到oid 在取数据
    uid = request.session.get("uid")

    return render(request,'order/user_center_order.html')

@filt
def ordersite(request):
    uid = request.session.get("uid")
    uu = User.objects.get(id=uid)
    return render(request,'order/user_center_site.html',{'uu':uu})




