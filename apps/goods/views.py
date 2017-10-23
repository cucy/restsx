from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import GoodsSerializer
from .models import Goods


class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
    """
    商品列表页.
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
