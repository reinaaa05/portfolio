from django.db import models
from django.utils import timezone

class Diary(models.Model):
    category = models.CharField('カテゴリ', max_length=225)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
      return 'カテゴリ:{} 本文:{}' .format(self.category,self.text[:10])