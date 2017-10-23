#!/usr/bin/env python
# _*_ coding:utf8 _*_
from django.db.models import Q

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
    name = django_filters.filters.CharFilter(name="name", lookup_expr='icontains')  # 忽略大小写

    top_category = django_filters.NumberFilter(method='top_category_filter') # 自定义过滤器

    def top_category_filter(self, queryset, name, value):
        # 自定义过滤器 GET /goods/?top_category=1
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ["price_min", "price_max", "name"]
