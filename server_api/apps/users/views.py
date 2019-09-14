from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserFilter
from rest_framework import response

User = get_user_model()

# admin Blink@123 ; blink 123123

class UserViewset(viewsets.ReadOnlyModelViewSet):
    '''
    retrieve:
        返回指定用户信息
    list:
        返回用户列表
    '''

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # pagination_class = PageNumberPagination
    # pagination_class = None

    # def get_queryset(self):
    #     queryset = super(UserViewset, self).get_queryset()
    #     username = self.request.query_params.get('username', None)
    #     if username:
    #         queryset = queryset.filter(username__icontains=username)
    #     return queryset

    # filter_backends = (DjangoFilterBackend,)
    filter_class = UserFilter
    filter_fields = ("username",)
    # authentication_classes = (SessionAuthentication, ) # 认证
    # permission_classes = (IsAuthenticated,) #

    # 增加用户自定义权限列表
    # 下面不能用
    # extra_perm_map = {
    #     'GET': ['auth.view_user'],
    # }


class DashboardStatusViewset(viewsets.ViewSet):
    '''

    '''
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        data = {
            'aa': 11,
            'bb': 22
        }
        return response.Response(data)

class UserInfoViewset(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        print(request.header, 'header -----')
        data = {
            "username": "admin",
            "name": "rock"
        }
        return response.Response(data)