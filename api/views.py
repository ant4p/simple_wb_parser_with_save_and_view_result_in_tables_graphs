from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from api.filters import ProductFilterAPI
from api.serializers import ProductsSerializer
from products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilterAPI
