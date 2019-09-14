from rest_framework import serializers
from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(GroupSerializer, self).to_representation(instance)
        ret['users'] = instance.user_set.count()
        return ret


    class Meta:
        model = Group
        fields = ("id", "name")