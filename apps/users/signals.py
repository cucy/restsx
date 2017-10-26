#!/usr/bin/env python
# _*_ coding:utf8 _*_ 
__date__ = '2017/10/26 20:42'
__author__ = 'zhourudong'

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()
# 信号文件   x

@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()
