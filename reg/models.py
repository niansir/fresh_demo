from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=10)
    upassword = models.CharField(max_length=50)
    uemail = models.CharField(max_length=20)
    uphone = models.BigIntegerField(null=True)
    usname = models.CharField(max_length=20,null=True)
    uaddress = models.CharField(max_length=60,null=True)
    uregister_time = models.DateTimeField()

    def __str__(self):
        return "%s,%s" % (self.id,self.uname)



