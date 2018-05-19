"""fresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include,re_path
from goods import views
urlpatterns = [
    url('detail/',views.detail),
    re_path('(?P<type>[0-9]{1,3})/(?P<page>[0-9]{1,3})/(?P<sort>[0-9]{1,3})/$',views.list),
    re_path('(?P<gc>[0-9]{1,10})/(?P<gid>[0-9]{1,10})/$',views.goods_info),
]
