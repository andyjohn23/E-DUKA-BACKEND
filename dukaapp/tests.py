from django.test import TestCase
from .models import Category,Sub_Category,Shop,Product,Comment,Order,User

class Test_Create_Shop(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create('electronics')
        test_sub_category = Sub_Category.objects.create('laptops')
        test_user1 = User.objects.create(first_name='collins',last_name='kipkoech',email='colo@gmail.com',
        password='colo1234')
        test_product = Product.objects.create(description='Hp laptop',item_name='laptop',price=5000,
        comment='nice product')
        test_shop = Shop.objects.create(description='electronics shop',category='electronics',merchant_name='collins')
        test_comment = Comment.objects.create(comment='nice product',user_id=1,product_id=1)
        test_order = Order.objects.create(user='collins',product_id=1)


    # def test_product_content(self):

        

