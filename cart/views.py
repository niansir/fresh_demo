from django.shortcuts import render,redirect
from cart.models import carttable
from comments.filter_user import filt
from django.http import JsonResponse
from goods.models import goods
from django.db.models import F

# Create your views here.
@filt
def cartku(request):
    user_id = request.session.get('uid','')
    carts = carttable.objects.filter(uid=user_id)
    context = {
        'carts':carts
    }
    return render(request,'cart/cart.html',context)
@filt
def add(request,gid,count):
    ggid = int(gid)
    uuid = request.session.get('uid','')
    carts = carttable.objects.filter(uid_id=uuid,gid_id=ggid)
    # 只可能对应一条记录，所以这里取出来数量加一即可
    if(len(carts)>=1):
        carttable.objects.filter(uid_id=uuid,gid_id=ggid).update(count=F('count')+int(count))
    else:
        cc = carttable()
        cc.gid_id = ggid
        cc.uid_id = uuid
        cc.count = count
        cc.save()
    if request.is_ajax():
        count = carttable.objects.filter(uid=request.session.get('uid')).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/buy/')

def edit(request,cid,count):
    count = int(count)
    state = carttable.objects.filter(gid=cid,uid=request.session.get('uid')).update(count=count)
    if(state):
        return JsonResponse({'state':0})
    else:
        return JsonResponse({'state':state})

def delete(request,cid):
    state = carttable.objects.filter(gid=cid,uid=request.session.get('uid')).delete()
    if(state):
        return JsonResponse({'state':0})
    else:
        return JsonResponse({'state':state})