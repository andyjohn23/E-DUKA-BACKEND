from django.test import TestCase,SimpleTestCase
from rest_framework.test import APITestCase
from .models import Category,Sub_Category,Shop,Product,Order,Comment,Profile,User
from django.urls import reverse,resolve
from rest_framework import status
import json
from rest_framework.authtoken.models import Token
from .serializer import ProfileSerializer
from .views import ProductDetail

class ShopTestCase(TestCase):

    # Set up method
    def setUp(self):
        self.shop1= Shop.objects.create(merchant_name='collins',description='electronics shop')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.shop1,Shop))

    # Testing Save Method
    def test_save_shop(self):
        self.shop1.save_shop()
        shops = Shop.objects.all()
        self.assertTrue(len(shops) > 0)
class CategoryTestCase(TestCase):
    
    def setUp(self):
        self.shop1= Shop.objects.create(merchant_name='collins',description='electronics shop')
        self.category1= Category.objects.create(category='electronics',image='avatar.png',card='card.png',shop=self.shop1)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category1,Category))

    def test_save_category(self):
        self.category1.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category1.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) - 1)

class SubCategoryTestCase(TestCase):
    
    def setUp(self):
        self.shop1= Shop.objects.create(merchant_name='collins',description='electronics shop')
        self.category1= Category.objects.create(category='electronics',image='avatar.png',card='card.png',shop=self.shop1)
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
    
class ProductTestCase(TestCase):
    
    def setUp(self):
        self.shop1= Shop.objects.create(merchant_name='collins',description='electronics shop')
        self.category1= Category.objects.create(category='electronics',image='avatar.png',card='card.png',shop=self.shop1)
        self.sub_category1= Sub_Category.objects.create(name='laptops',description='brand new HP laptops',category=self.category1)
        self.product1 = Product.objects.create(item_name='laptop',description='HP corei5, 2GB RAM',price=40000,
        image='avatar.png',shipped_from='e-duka',color='black',quantity=0,sub_category=self.sub_category1,
        previous_price=35000,size='12 inches',brand='HP')
    
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

class CommentTestCase(TestCase):
     
    def setUp(self):
        self.shop1= Shop.objects.create(merchant_name='collins',description='electronics shop')
        self.category1= Category.objects.create(category='electronics',image='avatar.png',card='card.png',shop=self.shop1)
        self.sub_category1= Sub_Category.objects.create(name='laptops',description='brand new HP laptops',category=self.category1)
        self.product1 = Product.objects.create(item_name='laptop',description='HP corei5, 2GB RAM',price=40000,
        image='avatar.png',shipped_from='e-duka',color='black',quantity=0,sub_category=self.sub_category1,
        previous_price=35000,size='12 inches',brand='HP')
        self.user1 = User.objects.create_user(first_name='collins',last_name='kipkoech',email='colo@gmail.com')
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


class OrderTestCase(TestCase):
    
    
    def setUp(self):
        self.shop1= Shop.objects.create(merchant_name='collins',description='electronics shop')
        self.category1= Category.objects.create(category='electronics',image='avatar.png',card='card.png',shop=self.shop1)
        self.sub_category1= Sub_Category.objects.create(name='laptops',description='brand new HP laptops',category=self.category1)
        self.product1 = Product.objects.create(item_name='laptop',description='HP corei5, 2GB RAM',price=40000,
        image='avatar.png',shipped_from='e-duka',color='black',quantity=0,sub_category=self.sub_category1,
        previous_price=35000,size='12 inches',brand='HP')
        self.user1 = User.objects.create_user(first_name='collins',last_name='kipkoech',email='colo@gmail.com')
        self.order1 = Order.objects.create(user=self.user1,product_id=self.product1,delivered=1)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.order1,Order))

    def test_save_order(self):
        self.order1.save_order()
        orders = Order.objects.all()
        self.assertTrue(len(orders) > 0)

    def test_delete_order(self):
        self.order1.delete_order()
        orders = Order.objects.all()
        self.assertTrue(len(orders) - 1)

class UserTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(first_name='collins',last_name='kipkoech',email='colo@gmail.com')  
    
    def test_instance(self):
        self.assertTrue(isinstance(self.user1,User))

############################################################################
                    # URLS tests
############################################################################
class UrlsTestCase(TestCase):
    def test_products_url(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code,200)

    def test_comments_url(self):
        response = self.client.get(reverse('comments'))
        self.assertEqual(response.status_code,200)

    def test_orders_url(self):
        response = self.client.get(reverse('orders'))
        self.assertEqual(response.status_code,200)
    
    def test_categories_url(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code,200)

    def test_shops_url(self):
        response = self.client.get(reverse('shops'))
        self.assertEqual(response.status_code,200)




    
  
############################################################################
                    # view tests
############################################################################

class RegistrationTestCase(APITestCase):
    def test_user_can_register_with_no_data(self):
        register_url = reverse('user_signup')
        response = self.client.post(register_url)
        self.assertEqual(response.status_code,400)

    def test_user_can_register_with_data(self):
        url = reverse('user_signup')
        user_data = {
            'first_name':'collins',
            'last_name':'kipkoech',
            'email':'test@gmail.com',
            'password':'test1234',
            
        }
        response = self.client.post(url,user_data,format='json')
        self.assertEqual(response.status_code,200)


       








    

    






