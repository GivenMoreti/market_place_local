from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')  # Each user can review a product only once

    def __str__(self):
        return f"{self.user.username} rated {self.product.title} {self.rating}/5"
