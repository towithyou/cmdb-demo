from django.db import models
from idcs.models import Idc
# Create your models here.

# 机柜
class Cabinet(models.Model):
    idc = models.ForeignKey(Idc, verbose_name="所在机房", null=False)
    name = models.CharField('机柜名', max_length=255)
    # 扩展字段后期加

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resources_cabinet'
        ordering = ['id']