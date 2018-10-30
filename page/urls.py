from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns("",
                       ## первый вариант

                       # url(r'^$', views.index, name="index"),
                       # url(r'^good/$', views.good, name="good"),

                       ## второй вариант

                       # url(r'^(?:\?id=(?P<id>\d+))?$', views.good, name="index"),
                       # url(r'^good/\?id=(?P<id>\d+)$', views.good, name="good"),

                       # третий вариант

                       url(r'^(?:\?id=(?P<id>\d+)/)?$', views.good, name="index"),
                       url(r'^good/(?P<id>\d+)/$', views.good, name="good"),

                       )
