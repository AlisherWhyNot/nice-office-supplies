from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CommentViewSet, ProductViewSet

router = DefaultRouter()

router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
