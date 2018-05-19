from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include,re_path
from order import views
urlpatterns = [
    re_path('index/',views.orderinfod),
    re_path('^orderhead/',views.orderheader),
    re_path('^orderlist/',views.orderlist),
    re_path('^ordersite/',views.ordersite)
]
