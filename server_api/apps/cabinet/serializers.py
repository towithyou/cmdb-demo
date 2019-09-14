from rest_framework import serializers
from idcs.serializers import IdcSerializer
from .models import Cabinet
from idcs.models import Idc


class CabinetSerializer(serializers.Serializer):
    # idc = IdcSerializer(many=False)
    idc = serializers.PrimaryKeyRelatedField(many=False, queryset=Idc.objects.all()) # 主键关联 many 如果当前一条记录对应的是多条记录是true,单条是false
    # idc = serializers.SerializerMethodField() # 只读，不可以（反序列化和提交数据）用这个字段
    name = serializers.CharField(required=True)

    # def get_idc(self, obj):
    #     '''
    #     只读
    #     :param obj:
    #     :return:
    #     '''
    #     print(obj)
    #     print(obj.idc)
    #     ret= {
    #         'id': obj.idc.id,
    #         'name': obj.idc.name
    #     }
    #     return ret


    def to_internal_value(self, data): # 序列化前验证 反序列化
        """
        反序列化验证的第一步
        反序列化第一步：拿到的是原始，提交过来的数据 queryDict
        :param data:
        :return:
        """
        print(data, 'to_internal_value.....')
        return super(CabinetSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        # 把上面定义的成员属性，序列化为标准的json，字典的类型是上面定义的
        # print(instance) # 这里是机柜对象
        # print(type(instance))
        # print(instance.idc, type(instance.idc))
        # ret = super(CabinetSerializer, self).to_representation(instance)
        # ret['aaa'] = 'bbb'
        idc_obj = instance.idc
        ret = super(CabinetSerializer, self).to_representation(instance)
        ret['idc'] = {
            'id': idc_obj.id,
            'name': idc_obj.name
        }
        return ret

    def create(self, validated_data):
        # raise serializers.ValidationError('create error')
        print(validated_data)
        return Cabinet.objects.create(**validated_data)