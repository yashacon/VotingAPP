from django.db import models
# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=200)
    count=models.IntegerField(default=0)
    def __str__(self):
        return 'Item {} is voted {}'.format(self.title, self.count)

class Voted(models.Model):
    username=models.CharField(max_length=200)
    def __str__(self):
        return self.username