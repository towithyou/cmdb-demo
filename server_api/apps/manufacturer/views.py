
from rest_framework import viewsets
from .serializers import ManufacturerSerializer, ProductModelSerializer
from .models import Manufacturer, ProductModel
# Create your views here.



class ManufacturerViewset(viewsets.ModelViewSet):
    '''
    retrieve:
        返回指定制造商信息
    list:
        返回制造商列表
    update:
        更新制造商信息
    destroy:
        删除制造商记录
    create:
        创建制造商记录
    partial_update:
        更新部分记录
    '''

    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ProductModelViewset(viewsets.ModelViewSet):
    '''
    retrieve:
        返回指定型号信息
    list:
        返回型号列表
    update:
        更新型号信息
    destroy:
        删除型号记录
    create:
        创建型号记录
    partial_update:
        更新部分记录
    '''

    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer


