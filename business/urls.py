from django.urls import path
from .views import (
    BusinessListCreate,
    BusinessRetrieveUpdateDestroy,
  
)
urlpatterns = [
    path('business/', BusinessListCreate.as_view(), name='room-list-create'),
    path('business/<int:pk>/', BusinessRetrieveUpdateDestroy.as_view(), name='room-retrieve-update-destroy'),
]
