from rest_framework import serializers
from .models import Idc

class IdcSerializer(serializers.Serializer):
    '''
    Idc 序列化类
    '''


    id = serializers.IntegerField(read_only=True) # 客户端提交id 忽略，只读的
    name = serializers.CharField(required=True,
                                 max_length=32,
                                 min_length=2,
                                 label='机房名称',
                                 help_text='机房名称',
                                 error_messages={'blank': '机房名称不能为空', 'required': '这个字段必填'}) # 客户端必须传,不能为空 <2<32
    address = serializers.CharField(required=True,
                                    max_length=256,
                                    label='机房地址',
                                    help_text='机房地址',
                                    error_messages={'blank': '机房地址不能为空', 'required': '这个字段必填'})
    phone = serializers.CharField(required=True, max_length=15, label='联系电话', help_text='联系电话')
    email = serializers.EmailField(required=True, label='邮箱email', help_text='email')
    letter = serializers.CharField(required=True, max_length=5, label='机房简称', help_text='机房简称')

    def create(self, validated_data):
         return Idc.objects.create(**validated_data) # 返回一个数据实例


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.letter = validated_data.get('letter', instance.letter)
        instance.save()
        return instance