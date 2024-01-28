from django.urls import path
from .views import (ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete, subscriptions)
                    # create_product)


urlpatterns = [
   path('', ProductsList.as_view(), name='product_list'),
   path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
   # path('create/', create_product, name='product_create'),
   path('create/', ProductCreate.as_view(), name='product_create'),
   path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
   path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
   path('subscriptions/', subscriptions, name='subscriptions')
]