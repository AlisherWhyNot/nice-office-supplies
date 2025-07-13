from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from products.models import Category, Comment, Product

from .permissions import CanCreateEditDeleteComments
from .serializers import (CategorySerializer, CommentSerializer,
                          ProductCreateSerializer, ProductListSerializer,
                          ProductSerializer)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'code'
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'code')


    @action(detail=False, url_path='recent-new-products')
    def recent_new_products(self, request):
        """Gives last five new products"""
        last_products = Product.objects.all()[:5]
        serializer = self.get_serializer(last_products, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'create':
            return ProductCreateSerializer
        return ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CanCreateEditDeleteComments]
    throttle_classes = (AnonRateThrottle,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
