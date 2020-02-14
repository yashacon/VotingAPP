from django.db import models
from django.contrib.auth.models import User

import os

def get_upload_path(instance, filename):
    fileName, fileExtension = os.path.splitext(filename)
    return os.path.join(
      "user_%s" % instance.user.username,"user_{0}.{1}" .format(instance.user.username,fileExtension) )

# Create your models here.
class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    display_picture=models.ImageField(upload_to=get_upload_path)
    has_voted=models.BooleanField(default=False)
    voted_item=models.CharField(max_length=200,default='none')
    def __str__(self):
        return self.user.username



class Item(models.Model):
    title=models.CharField(max_length=200)
    count=models.IntegerField(default=0)
    def __str__(self):
        return 'Item {} is voted {}'.format(self.title, self.count)
