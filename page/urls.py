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

                       # url(r'^(?:\?id=(?P<cat_id>\d+)/)?$', views.index, name="index"),
                       url(r'^(?:(?P<cat_id>\d+)/)?$', views.index, name="index"),
                       url(r'^good/(?P<good_id>\d+)/$', views.good, name="good"),

                       )
