from django.db import models

# Create your models here.

class User(models.Model):
    name=models.TextField()
    email=models.TextField()
    phno=models.TextField()
    username=models.TextField()
    password=models.TextField()
    profile_img=models.FileField(null=True)


class Post(models.Model):
    uname=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.FileField()
    desc=models.TextField()
