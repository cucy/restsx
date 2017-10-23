from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import GoodsSerializer
from .models import Goods


class GoodsListView(APIView):
    """
    List all goods.
    """

    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)  # many=True 因为goods是列表
        return Response(goods_serializer.data)     # serializer.data 实例serializer后的数据
