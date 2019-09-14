from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from .serializers import IdcSerializer
from .models import Idc

########################## version 1 ########################
class JsonResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        data = JSONRenderer().render(data)
        super(JsonResponse, self).__init__(content=data, **kwargs)


def idc_list(request: HttpRequest, *args, **kwargs):
    if request.method == 'GET':
        print('get list all')
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
        # content = JSONRenderer().render(serializer.data)
        # return HttpResponse(content, content_type='application/json')

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IdcSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            print('验证通过')
            serializer.save()
            return JsonResponse(serializer.data)


def idc_detail(request: HttpRequest, pk, *args, **kwargs):
    try:
        print(pk)
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist as e:
        print(e)
        ret = {
            'error': "not found"
        }
        return JsonResponse(ret, status=404)
    except Exception as e:
        print('Exception  ~~~~~~~~')
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer =  IdcSerializer(idc)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        print('put', '++++++++++++++++++++++++++++++++++++++++++++++')
        data = JSONParser().parse(request)
        print(data, '---------')
        serializer = IdcSerializer(idc, data=data)

        # if serializer.is_valid(): # 必须要验证才可以查看原来的数据
        #     print(serializer.data, 'XXXXXXXXXXXXXXXXXXXXXX')
        # return HttpResponse('OK')
        try:
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        except Exception as e:
            print(e)
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        idc.delete()
        msg = {
            'msg': 'delete success'
        }
        return JsonResponse(msg, status=204)

########################  version  2  ##########################
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def idc_list_v2(request: HttpRequest, *args, **kwargs):

    if request.method == 'GET':
        idc = Idc.objects.all()
        serializer = IdcSerializer(idc, many=True) # -> bytes
        print(serializer, 'bytes')
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = IdcSerializer(data=request.data) # 存 -> dict
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def idc_detail_v2(request: HttpRequest, pk, *args, **kwargs):

    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist as e:
        print(e)
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IdcSerializer(idc)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        print(request.data, type(request.data), 'putputput================================')
        serializer = IdcSerializer(idc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        idc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

from rest_framework.reverse import reverse
@api_view(["GET"])
def api_root(request: HttpRequest, format=None, *args, **kwargs):
    return Response({
        'idcs': reverse('v2_list', request=request, format=format)
    })


########################  version  3  ##########################

class IdcList_V3(APIView):

    def get(self, request: HttpRequest, format=None):
        idc = Idc.objects.all()
        serializer = IdcSerializer(idc, many=True)  # -> bytes
        return Response(serializer.data)

    def post(self, request: HttpRequest, format=None):
        serializer = IdcSerializer(data=request.data)  # 存 -> dict
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

from django.http import Http404
class IdcDetail_V3(APIView):

    def get_obj(self, pk):
        try:
            return Idc.objects.get(pk=pk)
        except Idc.DoesNotExist as e:
            raise Http404

    def get(self, request, pk, format=None):
        idc = self.get_obj(pk)
        serializer = IdcSerializer(idc)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        idc = self.get_obj(pk)
        serializer = IdcSerializer(idc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        idc = self.get_obj(pk)
        idc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

########################  version  4  ##########################
from rest_framework import mixins, generics

class IdcList_V4(generics.GenericAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class IdcDetail_V4(generics.GenericAPIView,
                   mixins.RetrieveModelMixin, # 只获取一条
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

########################  version  5  ##########################

class IdcList_V5(generics.ListCreateAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

class IdcDetail_V5(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


########################  version  6  ##########################
from rest_framework import viewsets

class IdcListViewSet_666(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.CreateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

########################  version  7  ##########################
class IdcViewSet_777(viewsets.ModelViewSet):
    '''
    retrieve:
        返回指定IDC信息
    list:
        返回IDC列表
    update:
        更新IDC信息
    destroy:
        删除IDC记录
    create:
        创建IDC记录
    partial_update:
        更新部分记录
    '''
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer