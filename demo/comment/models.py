from django.db import models
from booktest.models import Post

# Create your models here.

class Comment(models.Model):
    name=models.CharField(max_length=20)
    eml=models.EmailField(blank=True,null=True)
    url=models.URLField(blank=True,null=True)
    content=models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

