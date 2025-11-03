from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('姓名',max_length=20)
    avatar = models.ImageField('头像', upload_to='team',help_text='建议尺寸为500*755')
    title = models.CharField('职务',max_length=20)
    rank = models.IntegerField()

    class Meta:
        db_table = 'team'
        verbose_name = '团队管理'
        verbose_name_plural = '团队管理'

    def __str__(self):
        return self.name
