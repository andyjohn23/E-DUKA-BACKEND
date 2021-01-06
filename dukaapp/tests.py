from django.test import TestCase
from .models import Category,Sub_Category,Shop,Product,Comment,Order,User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class Test_Create_Duka(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(category='electronics',image='avatar.png')
        test_sub_category = Sub_Category.objects.create(name='laptops',description='nice product',product_id=1,category=test_category)
        test_user1 = User.objects.create(first_name='collins',last_name='kipkoech',email='colo@gmail.com',
        password='colo1234')
        test_product = Product.objects.create(description='Hp laptop',item_name='laptop',price='5000',image='avatar.png',category_id=1)
        test_shop = Shop.objects.create(description='electronics shop',category_id=1,merchant_name='collins')
        test_comment = Comment.objects.create(comment='nice product',user_id=1,product_id=test_product)
        test_order = Order.objects.create(user=test_user1,product_id=test_product)


    def test_product(self):
        product = Product.objects.get(pk=1)
        category = Category.objects.get(pk=1)
        sub_category = Sub_Category.objects.get(pk=1)
        description = f'{product.description}'
        item_name = f'{product.item_name}'
        price = f'{product.price}'
        self.assertEqual(description,'Hp laptop')
        self.assertEqual(item_name,'laptop')
        self.assertEqual(price,'5000')
        
        self.assertEqual(str(product),'laptop')

    def test_shop(self):
        shop = Shop.objects.get(id=1)
        category = Category.objects.get(pk=1)
        merchant_name = f'{shop.merchant_name}'
        description = f'{shop.description}'
        self.assertEqual(merchant_name,'collins')
        self.assertEqual(description,'electronics shop')

    def test_category(self):
        cat = Category.objects.get(id=1)
        category = f'{cat.category}'
        # image = f'{cat.image.url}'
        self.assertEqual(category,'electronics')
        # self.assertEqual(image,'avatar.png')
        self.assertEqual(str(category),'electronics')
    
    def test_sub_category(self):
        cat = Category.objects.get(id=1)
        sub_cat = Sub_Category.objects.get(id=1)
        name = f'{sub_cat.name}'
        description = f'{sub_cat.description}'
        category = f'{sub_cat.category}'
        self.assertEqual(name,'laptops')
        self.assertEqual(description,'nice product')
        self.assertEqual(category,'electronics')
        self.assertEqual(str(name),'laptops')

    def test_comment(self):
        comment1 = Comment.objects.get(id=1)
        comment = f'{comment1.comment}'
        self.assertEqual(comment,'nice product')
        self.assertEqual(str(comment),'nice product')


    
    



# class ProductsTests(APITestCase):

#     def test_view_products(self):
#         url = reverse('products')
#         response = self.client.get(url,format='json')
#         self.assertEqual(response.status_code,status.HTTP_200_OK)

