from django.urls import path
from .views import (
    FavoriteListCreate,
    FavoriteRetrieveUpdateDestroy,
  
)
urlpatterns = [
    path('favorites/', FavoriteListCreate.as_view(), name='favorite-list-create'),
    path('favorite/<int:pk>/', FavoriteRetrieveUpdateDestroy.as_view(), name='favorite-retrieve-update-destroy'),
]
