from django.db import models

# Create your models here.
class Shop(models.Model):
    merchant_name = models.CharField(max_length=100)
    business_description = models.TextField()
    date_started = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='category')