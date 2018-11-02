from django.conf.urls import patterns, url, include
from . import views
from .twviews import GoodListView, GoodDetailView

urlpatterns = patterns("",
                       ## первый вариант

                       # url(r'^$', views.index, name="index"),
                       # url(r'^good/$', views.good, name="good"),

                       ## второй вариант

                       # url(r'^(?:\?id=(?P<id>\d+))?$', views.good, name="index"),
                       # url(r'^good/\?id=(?P<id>\d+)$', views.good, name="good"),

                       # третий вариант

                       # url(r'^(?:\?id=(?P<cat_id>\d+)/)?$', views.index, name="index"),
                       # url(r'^(?:(?P<cat_id>\d+)/)?$', views.index, name="index"),
                       # url(r'^good/(?P<good_id>\d+)/$', views.good, name="good"),
                       url(r'^(?:(?P<cat_id>\d+)/)?$', GoodListView.as_view(), name="index"),
                       url(r'^good/(?P<good_id>\d+)/$', GoodDetailView.as_view(), name="good"),
                       )
