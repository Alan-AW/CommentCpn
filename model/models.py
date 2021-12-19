from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=24, verbose_name='用户名')
    pwd = models.CharField(max_length=64, verbose_name='密码')
    avatar = models.CharField(max_length=256, null=True)
    nickname = models.CharField(max_length=18, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'


class Article(models.Model):
    title = models.CharField(max_length=36, verbose_name='标题')
    content = models.TextField(verbose_name='内容')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
