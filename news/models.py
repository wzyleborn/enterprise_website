from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('分类名称',max_length=20)

    class Meta:
        db_table = 'category'
        verbose_name = '分类管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('标题',max_length=100)
    content = RichTextUploadingField()
    cover = models.ImageField('封面', upload_to='news', blank=True, null=True, help_text='建议上传480*270图片')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'news'
        verbose_name = '新闻管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title