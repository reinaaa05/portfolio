from django.db import models
from django.urls import reverse_lazy


class BaseModel(models.Model):
    create_at = models.DateField()
    update_at = models.DateField()

    class Meta:
        abstract = True

class Books(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()

    class Meta:
        db_table = 'books'
    
    def get_absolute_url(self):
        return reverse_lazy('store:detail_book', kwargs={'pk': self.pk})

class PicturesManager(models.Manager):
    def filter_by_book(self, book):
        return self.filter(book=book).all()

class Pictures(BaseModel):
    picture = models.FileField(upload_to='picture/')
    book = models.ForeignKey(
        'books', on_delete=models.CASCADE
    )
    objects = PicturesManager()