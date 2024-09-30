from django.urls import path
from .views import (
    ProductListCreate,
    ProductRetrieveUpdateDestroy,
  
)
urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='room-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='room-retrieve-update-destroy'),
]