from django.contrib import admin
from cart.models import carttable
# Register your models here.

class cartAdmin(admin.ModelAdmin):
    list_display = ['uid','gid','count']



admin.site.register(carttable,cartAdmin)
