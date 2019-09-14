from rest_framework import serializers
from .models import Manufacturer, ProductModel

from collections import OrderedDict

class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = '__all__'

class ProductModelSerializer(serializers.ModelSerializer): # 这个类实现了create方法，并且把model的中文显示
    class Meta:
        model = ProductModel
        fields = '__all__'

    def validate_model_name(self, value:str):
        print(value, '-------')
        print(type(value))
        return value

    def validate(self, attrs:OrderedDict):
        # 从业务上面说，厂商下面已经存在的型号不能重复，不通过model来解决，通过序列化，验证数据的时候来解决
        print(attrs, '++++++++++++++')
        print(type(attrs))
        try:
            manufacturer: Manufacturer = attrs['vendor']
            manufacturer.productmodel_set.filter(model_name__exact=attrs['model_name'])
            # 如果找到说明重复了
            raise serializers.ValidationError('该型号已经存在')
        except ProductModel.DoesNotExist as e:
            print(e)
            return attrs


    def to_representation(self, instance):
        vendor = instance.vendor
        print(vendor, type(vendor))
        ret = super(ProductModelSerializer, self).to_representation(instance)
        ret['vendor'] = {
            'id': vendor.id,
            'name': vendor.vendor_name
        }
        return ret