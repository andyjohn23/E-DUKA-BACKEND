from django.test import TestCase
from .models import Category,Sub_Category,Shop,Product,Order,Comment,Profile,User


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

    #Testing delete method
    def test_delete_category(self):
        self.category1.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) - 1)

class SubCategoryTestClass(TestCase):
    
    
    def setUp(self):
        self.category1= Category.objects.create(category='electronics',image='avatar.png')
        self.sub_category1= Sub_Category.objects.create(name='laptops',description='brand new HP laptops',category=self.category1)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.sub_category1,Sub_Category))

    
    def test_save_sub_category(self):
        self.sub_category1.save_sub_category()
        sub_categories = Sub_Category.objects.all()
        self.assertTrue(len(sub_categories) > 0)
    
    def test_delete_sub_category(self):
        self.sub_category1.delete_sub_category()
        sub_categories = Sub_Category.objects.all()
        self.assertTrue(len(sub_categories) - 1)
    
class ProductTestClass(TestCase):
    
    
    def setUp(self):
        self.category1= Category.objects.create(category='electronics',image='avatar.png')
        self.sub_category1= Sub_Category.objects.create(name='laptops',description='brand new HP laptops',category=self.category1)
        self.product1 = Product.objects.create(item_name='laptop',description='HP corei5, 2GB RAM',price=40000,image='avatar.png',sub_category=self.sub_category1)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.product1,Product))

    

    def test_save_product(self):
        self.product1.save_product()
        products = Product.objects.all()
        self.assertTrue(len(products) > 0)

    def test_delete_product(self):
        self.product1.delete_product()
        products = Product.objects.all()
        self.assertTrue(len(products) - 1)


class CommentTestClass(TestCase):
    
    
    def setUp(self):
        self.category1= Category.objects.create(category='electronics',image='avatar.png')
        self.sub_category1= Sub_Category.objects.create(name='laptops',description='brand new HP laptops',category=self.category1)
        self.product1 = Product.objects.create(item_name='laptop',description='HP corei5, 2GB RAM',price=40000,image='avatar.png',sub_category=self.sub_category1)
        self.user1 = User.objects.create(first_name='collins',last_name='kipkoech',email='colo@gmail.com')
        self.comment1 = Comment.objects.create(user=self.user1,product_id=self.product1)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.comment1,Comment))

    

    def test_save_comment(self):
        self.comment1.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comment(self):
        self.comment1.delete_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) - 1)






