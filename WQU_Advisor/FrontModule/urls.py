'''
Created on 2016. 12. 19.

@author: thcho
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^wquadvisor/$', views.marketScreen, name='marketScreen'),
    url(r'^wquadvisor/tradingStrategy/backTest/$', views.backTest, name='bakcTest')
#     url(r'^aiadvisor/backtest/$', views.backTestHome, name='backTestHome'),
#     url(r'^roboadvisor/backtest/$', views.backTestHome, name='backtest'),
#     url(r'^roboadvisor/backtest/results/$', views.results, name='strategyResults'),

#     url(r'^(?P<code>\w+)/$', views.stock_detail, name = 'stock_detail'),
#     url(r'^(?P<code>\w+)/$', views.stock_detail2, name = 'detail_imsi'),
#     url(r'^(?P<code>\w+)/$', views.ahomorgetta.stock_detail_class, name = 'chartdetailwithclass'),
#     url(r'^json/(?P<code>\w+)/$', views.stock_data_json, name = 'stock_data_json'),
#     url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name = 'post_detail'),
#     url(r'^post/new/$', views.post_new, name = 'post_new'),
#     url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit')
]
