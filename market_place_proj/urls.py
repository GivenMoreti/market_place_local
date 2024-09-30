from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/business/', include('business.urls')),
    path('api/products/', include('product.urls')),
    # path('api/reviews/', include('review.urls')),
    path('api/orders/', include('order.urls')),
    # path('api/payments/', include('payment.urls')),
    path('api/favorites/', include('favorite.urls')),
    path('api/carts/', include('cart.urls')),
]