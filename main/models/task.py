from django.db import models
from django.contrib.auth.models import AbstractUser
from .users import users
# Create your models here.
class task(models.Model):
    task_id = models.AutoField(primary_key=True)
    who = models.ForeignKey(users,on_delete=models.CASCADE)
    description = models.TextField()
    complete = models.CharField(max_length=200,default='Not Yet')
    priority = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    deadline = models.DateTimeField()
    creat_at = models.DateTimeField()
