from django.test import TestCase
from .models import Category,Sub_Category,Shop,Product,Order,Comment,Profile


class CategoryTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.category1= Category(category='electronics',image='avatar.png')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category1,Category))

    # Testing Save Method
    def test_save_method(self):
        self.category1.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

