#!/usr/bin/env python
# _*_ coding:utf8 _*_ 
__date__ = '2017/10/23 20:25'
__author__ = 'zhourudong'

import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤类
    """
    price_min = django_filters.filters.NumberFilter(name="shop_price", lookup_expr='gte')  # 大于等于
    price_max = django_filters.filters.NumberFilter(name="shop_price", lookup_expr='lte')  # 小于等于
    name = django_filters.filters.CharFilter(name="name", lookup_expr='icontains')  # 模糊查询忽略大小写

    class Meta:
        model = Goods
        fields = ["price_min", "price_max","name"]
