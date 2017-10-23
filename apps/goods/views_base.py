#!/usr/bin/env python
# _*_ coding:utf8 _*_
from django.views.generic.base import View
from goods.models import Goods

__date__ = '2017/10/23 16:34'
__author__ = 'zhourudong'


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return
        """
        
        goods = Goods.objects.all()[:10]

        import json
        from django.core import serializers
        from django.http import JsonResponse

        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)

        return JsonResponse(json_data, safe=False)  # 包含数组的时候设置 safe=False s
