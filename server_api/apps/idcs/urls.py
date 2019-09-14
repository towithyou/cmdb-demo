from django.conf.urls import url, include
from .views import idc_list, idc_detail
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

idc_list_V6 = views.IdcListViewSet_666.as_view({
    'get': 'list',
    'post': 'create'
})
idc_detail_V6 = views.IdcListViewSet_666.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

# 7
# from rest_framework.routers import DefaultRouter
# route = DefaultRouter()
# route.register('sss', views.IdcViewSet_777)
# urlpatterns = [
#     url(r'^', include(route.urls))
# ]
# urlpatterns = [
#     url(r'^$', views.api_root),
#     url(r'^idcs/v1/$', idc_list, name='v1_list'),
#     url(r'^idcs/v1/(\d+)/', idc_detail, name='v1_detail'),
#     url(r'^idcs/v2/$', views.idc_list_v2, name='v2_list'),
#     url(r'^idcs/v2/(\d+)/', views.idc_detail_v2, name='v2_detail'),
#     url(r'^idcs/v3/$', views.IdcList_V3.as_view(), name='v2_list'),
#     url(r'^idcs/v3/(\d+)/', views.IdcDetail_V3.as_view(), name='v2_detail'),
#     url(r'^idcs/v4/$', views.IdcList_V4.as_view(), name='v4_list'),
#     url(r'^idcs/v4/(?P<pk>\d+)/$', views.IdcDetail_V4.as_view(), name='v4_detail'),
#     url(r'^idcs/v5/$', views.IdcList_V5.as_view(), name='v4_list'),
#     url(r'^idcs/v5/(?P<pk>\d+)/$', views.IdcDetail_V5.as_view(), name='v4_detail'),
#     url(r'^idcs/v6/$', idc_list_V6, name='v6_list'),
#     url(r'^idcs/v6/(?P<pk>\d+)/$', idc_detail_V6, name='v6_detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)