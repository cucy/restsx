#!/usr/bin/env python
# _*_ coding:utf8 _*_ 
__date__ = '2017/10/23 17:25'
__author__ = 'zhourudong'
from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"


class CategorySerializer3(serializers.ModelSerializer):
    # 3级商品信息 
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    # 2级商品信息 嵌套3级
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    # 一级商品信息 嵌套二级
    sub_cat = CategorySerializer2(many=True)  # 通过一级拿到2级可能有多高many=True

    class Meta:
        model = GoodsCategory
        fields = "__all__"
