from django.test import TestCase
from .models import Category,Sub_Category,Shop,Product,Comment,Order,User

class Test_Create_Shop(TestCase):

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


    def test_product_content(self):
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



        

