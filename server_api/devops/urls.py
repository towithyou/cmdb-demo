"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^', include('idcs.urls'))
# ]

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from idcs.views import IdcViewSet_777
from users.views import UserViewset, DashboardStatusViewset
from cabinet.views import CabinetViewSet
# from rest_framework.schemas import AutoSchema
from manufacturer.views import ManufacturerViewset, ProductModelViewset
from servers.views import ServerAutoReportViewset, NetworkDevicelViewset, IPViewset, ServerViewset
from rest_framework_jwt.views import obtain_jwt_token


from groups.router import group_router

route = DefaultRouter()
route.register('idcss', IdcViewSet_777, base_name='ddd')
route.register('users', UserViewset, base_name='users')
route.register('cabinet', CabinetViewSet, base_name='cabinet')
route.register('Manufacturer', ManufacturerViewset, base_name='Manufacturer')
route.register('productModel', ProductModelViewset, base_name='productModel')
route.register('ServerAutoReport', ServerAutoReportViewset, base_name='ServerAutoReport')
route.register('NetworkDevicel', NetworkDevicelViewset, base_name='NetworkDevicel')
route.register('IP', IPViewset, base_name='IP')
route.register('Servers', ServerViewset, base_name='Servers')
route.register('DashboardStatus', DashboardStatusViewset, base_name='DashboardStatus')

route.registry.extend(group_router.registry)

urlpatterns = [
    url(r'^', include(route.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls('DHQ运维平台接口文档')),
    url('^api-token-auth/', obtain_jwt_token)
]
