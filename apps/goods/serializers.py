#!/usr/bin/env python
# _*_ coding:utf8 _*_ 
__date__ = '2017/10/23 17:25'
__author__ = 'zhourudong'
from rest_framework import serializers
from django.db.models import Q

from goods.models import Goods


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()
