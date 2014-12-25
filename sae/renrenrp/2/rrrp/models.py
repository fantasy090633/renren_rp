# coding=utf-8
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    flag = models.BooleanField()


class Log(models.Model):
    user = models.ForeignKey(User)
    log_info = models.TextField()