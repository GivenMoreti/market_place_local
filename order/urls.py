from django.urls import path
from .views import (
    OrderListCreate,
    OrderRetrieveUpdateDestroy,
  
)
urlpatterns = [
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroy.as_view(), name='order-retrieve-update-destroy'),
]
