from django.urls import path
from . import views

app_name="kate"

urlpatterns = [
    path("top/",views.qq,name="qq"),
    path("insuu/",views.ww,name="ww"),
    path("sinsuu/",views.ee,name="ee"),
    path("houtei1/",views.rr,name="rr"),
    path("houtei2/",views.tt,name="tt"),
    path("renritu/",views.yy,name="yy"),
    path("era/",views.uu,name="uu")
]