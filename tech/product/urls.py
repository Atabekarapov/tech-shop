from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import product_list,
# from .views import ProductsList, ProductDetail, \
#      CreateProduct, UpdateProduct, DeleteProduct
from .views import CategoriesList, ProductViewSet, CommentCreate


router = DefaultRouter()
router.register('', ProductViewSet)

# products = ProductViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'post': 'create',
#     'delete': 'destroy',
#     'get': 'retrieve'
# })

urlpatterns = [
    # path('', product_list),
    # path('', ProductsList.as_view()),
    # path('detail/<str:pk>/', ProductDetail.as_view()),
    # path('create/', CreateProduct.as_view()),
    # path('update/<str:pk>/', UpdateProduct.as_view()),
    # path('delete/<str:pk>/', DeleteProduct.as_view()),
    path('categories/', CategoriesList.as_view()),
    # path('', products),
    # path('<str:pk>/', products)
    path('', include(router.urls)),
    path('comments/create/', CommentCreate.as_view())
    ]
