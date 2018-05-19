from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20,primary_key=True)
    user = models.ForeignKey('reg.User',on_delete=models.CASCADE)
    odate = models.DateTimeField(auto_now=True)
    oispay = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    oaddress = models.CharField(max_length=200,default='')


class Orderdetailinfo(models.Model):
    gid = models.ForeignKey('goods.goods',on_delete=models.CASCADE)
    orid = models.ForeignKey(OrderInfo,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    count = models.IntegerField()

