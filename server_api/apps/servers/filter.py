import django_filters
from .models import Server
from django.db.models import Q


class ServerFilter(django_filters.FilterSet):
    hostname = django_filters.CharFilter(method="filter_hostname")

    def filter_hostname(self, qs, name, value):
        return qs.filter(Q(hostname__icontains=value) | Q(ip__icontains=value))

    class Meta:
        model = Server
        fields = ['hostname']