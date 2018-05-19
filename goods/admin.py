from django.contrib import admin
from goods.models import *
# Register your models here.
class gtypeAdmin(admin.ModelAdmin):
    list_display = ['id','gname']
    search_fields = ['gname',]


class gnameAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gname','gprice','gunit','gclick','gjianjie','gkucun']


admin.site.register(gtype,gtypeAdmin)
admin.site.register(goods,gnameAdmin)
