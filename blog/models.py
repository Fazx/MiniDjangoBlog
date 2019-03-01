from django.db import models
# import datetime

# timezone处理时间
from django.utils import timezone
# 导入内建的User模型
from django.contrib.auth.models import User


class Article(models.Model):
    # on_delete指定数据删除方式，避免两关联表数据不一致
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    # auto_now=True数据更新时自动写入当前时间
    update = models.DateTimeField(auto_now=True)

    class Meta:
        # 倒序排列
        ordering = ('-created',) # 元组不能遗漏逗号

    # 定义调用对象的str()方法时的返回值内容
    def __str__(self):
        return self.title