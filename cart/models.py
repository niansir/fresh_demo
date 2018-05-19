from django.db import models

# Create your models here.

class carttable(models.Model):
    uid = models.ForeignKey('reg.User',on_delete=models.CASCADE)
    gid = models.ForeignKey('goods.goods',on_delete=models.CASCADE)
    count = models.IntegerField(max_length=10)
    class Meta:
        verbose_name_plural = '购物车表'