from rest_framework import mixins, viewsets
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .filters import GoodsFilter

from .serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodsCategory


class GoodsResultsSetPagination(PageNumberPagination):
    """
    商品列表分页类
    """
    page_size = 10
    page_size_query_param = 'page_size'  # 每页只取3条数据的第二页 http://127.0.0.1:8000/goods/?page_size=3&q=2
    page_query_param = "q"  # 后边的 http://xxx/?p=1
    max_page_size = 100

# CacheResponseMixin 缓存功能

class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页.
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsResultsSetPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('name', 'shop_price')  # 过滤

    search_fields = ('^goods_desc', '=name', "goods_brief")  # 搜索   ^开头 =等于
    ordering_fields = ('sold_num', 'add_time')  # 排序

    filter_class = GoodsFilter

    # authentication_classes = (TokenAuthentication, )   # 对这个接口启用token认证功能
    # 公共的页面不应该配置 token认证


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
