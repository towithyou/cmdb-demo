from django.db import models

# Create your models here.

class Idc(models.Model):

    name = models.CharField("机房名称", max_length=32)
    address = models.CharField('机房地址', max_length=200)
    phone = models.CharField('机房联系电话', max_length=15)
    email = models.EmailField('机房练习email')
    letter = models.CharField('idc 字母简称', max_length=5)


class Manufacturer(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

class Car(models.Model):
    man = models.ForeignKey(Manufacturer)
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name