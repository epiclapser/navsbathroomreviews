from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS = ((0,'Draft'),(1,'Publish'))
class Review(models.Model):
    title = models.CharField(max_length=200,unique = False)
    slug  = models.SlugField(max_length=200,unique = True)
    updated_on = models.DateTimeField(auto_now = True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default = 0)

    def __str__(self):
        return self.title