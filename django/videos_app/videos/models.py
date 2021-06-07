from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings


class Category(models.Model):
   name = models.CharField('カテゴリ名', max_length=255, unique=True)
   
   def __str__(self):
      return self.name

class Video(models.Model):
   title = models.CharField('動画タイトル', max_length=255)
   thumbnail = models.ImageField('サムネイル',blank=True)
   file = models.FileField('動画ファイル', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'mpeg', 'mpg', 'avi', 'wmv', 'flv', ''])]
   )
   category = models.ForeignKey(Category,on_delete=models.PROTECT, verbose_name='カテゴリ',blank=True,null=True)
   writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='投稿者',blank=True,null=True)
   good = models.IntegerField('高評価',blank=True,null=True, default=0)
   goodtext = models.TextField(blank=True,null=True, default='a')
   bad = models.IntegerField('低評価',blank=True,null=True, default=0)
   badtext = models.TextField(blank=True,null=True, default='a')

   def __str__(self):
      return self.title 

class Comment(models.Model):
   text = models.TextField('本文')
   target = models.ForeignKey(Video, on_delete=models.PROTECT, verbose_name='どの記事へのコメントか')


   def __str__(self):
      return self.text[:20] 
