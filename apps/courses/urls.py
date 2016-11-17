from django.conf.urls import url
from . import views

#models--views--templates

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$',views.add),
    url(r'^delete/(?P<id>\d+)$',views.delete),
    url(r'^yesdelete/(?P<id>\d+)$',views.yesdelete)
]
