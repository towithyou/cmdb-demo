from django.contrib.auth.models import Group
from rest_framework import viewsets
from .serializers import GroupSerializer
from .filters import GroupFilter

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_class = GroupFilter
    filter_fields = ("name", )

