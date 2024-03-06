from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class users(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    join_at = models.DateTimeField()
class task(models.Model):
    task_id = models.AutoField(primary_key=True)
    who_id = models.ForeignKey(users,on_delete=models.CASCADE)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    priority = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    deadline = models.DateTimeField()
    creat_at = models.DateTimeField()
