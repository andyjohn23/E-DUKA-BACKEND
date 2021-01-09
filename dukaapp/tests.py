from django.test import TestCase
from .models import Category,Sub_Category,Shop,Product,Order,Comment,Profile


class CategoryTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.category1= Category.objects.create(category='electronics',image='avatar.png')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category1,Category))

    # Testing Save Method
    def test_save_category(self):
        self.category1.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class SubCategoryTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.category1= Category.objects.create(category='electronics',image='avatar.png')
        self.sub_category1= Sub_Category.objects.create(name='laptops',description='brand new HP laptops',category=self.category1)
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sub_category1,Sub_Category))

    # Testing Save Method
    def test_save_sub_category(self):
        self.sub_category1.save_sub_category()
        sub_categories = Sub_Category.objects.all()
        self.assertTrue(len(sub_categories) > 0)

# class ProfileTestClass(TestCase):
    
#     # Set up method
#     def setUp(self):
#         self.profile= Profile(category='electronics',image='avatar.png')
#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.category1,Category))

#     # Testing Save Method
#     def test_save_category(self):
#         self.category1.save_category()
#         categories = Category.objects.all()
#         self.assertTrue(len(categories) > 0)

