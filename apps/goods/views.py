from rest_framework import mixins, viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

from .serializers import GoodsSerializer
from .models import Goods


class GoodsResultsSetPagination(PageNumberPagination):
    """
    商品列表分页类
    """
    page_size = 10
    page_size_query_param = 'page_size'  # 每页只取3条数据的第二页 http://127.0.0.1:8000/goods/?page_size=3&q=2
    page_query_param = "q"  # 后边的 http://xxx/?p=1
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页.
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsResultsSetPagination

    def get_queryset(self):
        queryset = Goods.objects.all()
        price_min = self.request.query_params.get("price_min", 0)
        if price_min:
            queryset = queryset.filter(shop_price__gt=int(price_min) )
        return queryset
