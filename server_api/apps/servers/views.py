
from rest_framework import viewsets, mixins
from .serializers import ServerAutoReportSerializer, NetworkDeviceSerializer, IPSerializer, ServerSerializer
from .models import Server, NetworkDevice, IP
from .filter import ServerFilter

class ServerViewset(viewsets.ReadOnlyModelViewSet):
    '''
    retrieve:
        返回指定服务器信息
    list:
        返回定服务器信息列表
    '''
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_class = ServerFilter
    filter_fields = ("hostname",)

    # 自定义权限
    # extra_perm_map = {
    #     'GET': ['servers.view_server'],
    # }

class ServerAutoReportViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    create:
        创建服务器信息
    '''

    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer

class NetworkDevicelViewset(viewsets.ReadOnlyModelViewSet):
    '''
    retrieve:
        返回指定网卡信息
    list:
        返回定网卡信息列表
    '''

    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer


class IPViewset(viewsets.ReadOnlyModelViewSet):
    '''
    retrieve:
        返回指定IP信息
    list:
        返回IP信息列表
    '''

    queryset = IP.objects.all()
    serializer_class = IPSerializer