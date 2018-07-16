# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('treasure/',views.treasure, name='treasure'),
    path('addtreasure/',views.addtreasure, name='addtreasure'),
    path('img/',views.img, name='img'),
    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    # path('draw/treasure', views.treasure, name='treasure'),
]

