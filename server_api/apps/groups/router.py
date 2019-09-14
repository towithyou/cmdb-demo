from rest_framework.routers import DefaultRouter
from .views import GroupViewset

group_router = DefaultRouter()
group_router.register('Groups', GroupViewset, base_name='Groups')
