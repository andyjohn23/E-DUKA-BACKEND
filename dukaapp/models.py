from django.db import models

# Create your models here.
class Shop(models.Model):
    merchant_name = models.CharField(max_length=100)
    description = models.TextField()
    date_started = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='shop')

class Category(models.Model):
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey("Sub-Category", on_delete=models.CASCADE, related_name='category')
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

class Sub-Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='sub-category')

    def __str__(self):
        return self.name


class Product(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name='product')


    def __str__(self):
        return self.item_name

    def save_product(self):
        self.save()
