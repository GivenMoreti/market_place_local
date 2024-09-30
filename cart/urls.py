from django.urls import path
from .views import (
    CartListCreate,
    CartRetrieveUpdateDestroy,
  
)
urlpatterns = [
    path('carts/', CartListCreate.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartRetrieveUpdateDestroy.as_view(), name='cart-retrieve-update-destroy'),
]
