from django.db import models
from django.conf import settings as sys
from django.utils.module_loading import import_string


class Comment(models.Model):
    TYPE_OF = (
        (1, '文章评论'),
        (2, '留言'),
        (3, '其他'),
    )
    type = models.IntegerField(default=1, choices=TYPE_OF, verbose_name='指向哪里')
    if type == 1:
        article = models.ForeignKey(import_string(sys.ARTICLE_MODEL_CLASS), on_delete=models.CASCADE,
                                    verbose_name='如果该评论是指向文章的话那么就有值')
    else:
        article = models.IntegerField(default=0, verbose_name='如果该评论不是指向文章的话那么值为0', null=True)
    user = models.ForeignKey(import_string(sys.USER_MODEL_CLASS), on_delete=models.CASCADE, verbose_name='发表该评论的用户')
    date_joined = models.DateField(auto_now_add=True, verbose_name='发表评论的时间')
    content = models.TextField(verbose_name='评论内容')
    root = models.ForeignKey('self', related_name='rootC', on_delete=models.CASCADE, verbose_name='指向本条评论的根评论',
                             null=True)
    parent = models.ForeignKey('self', related_name='parentC', on_delete=models.CASCADE, verbose_name='指向本条评论的父级评论',
                               null=True)
    # replay = models.ForeignKey(import_string(sys.USER_MODEL_CLASS), related_name='repliesC', on_delete=models.CASCADE,
    #                            verbose_name='指向本条评论的回复对象', null=True)

    def __str__(self):
        return '%s：%s' % (self.user, self.content)

    class Meta:
        db_table = 'comment'
