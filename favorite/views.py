from rest_framework import generics
from .models import Favorite
from .serializers import FavoriteSerializer

class FavoriteListCreate(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer