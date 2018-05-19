#coding:utf-8
from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class gtype(models.Model):
    gname = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = '商品类型'

    def __str__(self):
        return self.gname

class goods(models.Model):
    gname = models.CharField(max_length=50)
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    gimage = models.ImageField(upload_to='static/df_goods')
    gunit = models.CharField(max_length=20,default='500g')
    gclick = models.IntegerField()
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcontent = HTMLField()
    gtype = models.ForeignKey(gtype,on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = '商品表'
    def __str__(self):
        return "%s,%s" %(self.gname,self.gtype.gname)