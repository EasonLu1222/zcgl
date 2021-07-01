from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# 定义用户模型，添加额外的字段
class UserProfile(AbstractUser):
    staff_no = models.CharField(max_length=15, verbose_name='工號', blank=True)
    department = models.CharField(max_length=15, verbose_name='部們', blank=True)
    isadmin = models.CharField(max_length=10, choices=(('1', '是'), ('0', '否')),
                               verbose_name='是否管理員', default='0', blank=True)
    bg_telephone = models.CharField(max_length=12, verbose_name='辦公室電話', blank=True)
    mobile = models.CharField(max_length=11, verbose_name='手機號碼', blank=True)
    is_superuser = models.IntegerField(verbose_name='是否超级管理員', default=0)
    is_staff = models.CharField(max_length=10, choices=(('1', '是'), ('0', '否')),
                                verbose_name='是否在職', default='1', blank=True)
    modify_time = models.DateTimeField(default=datetime.now, verbose_name='修改时間')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 定义用户操作日志模型
class UserOperateLog(models.Model):
    username = models.CharField(max_length=20, verbose_name='人員')
    scope = models.CharField(max_length=20, verbose_name='操作範圍')
    type = models.CharField(max_length=20, verbose_name='操作類型')
    content = models.IntegerField(verbose_name='操作内容')
    modify_time = models.DateTimeField(default=datetime.now, verbose_name='操作時間')

    class Meta:
        verbose_name = '用户操作日誌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username + '.' + self.type
