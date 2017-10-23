#!/usr/bin/env python
# _*_ coding:utf8 _*_ 
__date__ = '2017/10/23 17:25'
__author__ = 'zhourudong'
from rest_framework import serializers


from goods.models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"
