from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=20)
    time=models.DateTimeField(auto_now_add=True)
    reader=models.IntegerField()
    abstract=models.CharField(max_length=150)

class Discuss(models.Model):
    dname=models.CharField(max_length=20)
    ddiscuss=models.CharField(max_length=50)
    dtime=models.CharField(auto_created=True)
    articleid=models.ForeignKey('self',on_delete=models.CASCADE)

