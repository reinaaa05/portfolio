from django.db import models


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