from django.urls import path
from . import views
from django.conf.urls import url
from . import apis

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^login/', apis.login, name="login"),
    url(r'^product_list/$', apis.product_list, name="product_list"),
    url(r'^bid/$', apis.bid, name="bid"),
    url(r'^place_order/$', apis.place_order, name="bid")
]