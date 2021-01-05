from __future__ import unicode_literals

from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.
class Shop(models.Model):
    merchant_name = models.CharField(max_length=100)
    description = models.TextField()
    date_started = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='shop')

  
    def save_shop(self):
        self.save()

    def delete_delete(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey("Sub_Category", on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.name
    

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='sub_category')

    def __str__(self):
        return self.name
    
    def save_sub_category(self):
        self.save()

    def delete_sub_category(self):
        self.delete()


class Product(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name='product', null=True, blank=True)


    def __str__(self):
        return self.item_name

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()
        
class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  CUSTOMER = 1
  MERCHANT = 2
  ADMIN = 3
  ROLE_CHOICES = (
      (CUSTOMER, 'customer'),
      (MERCHANT, 'merchant'),
      (ADMIN, 'admin'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()
        



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        print("email...",email)
        print("password...",password)
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField( default=False)
    avatar = CloudinaryField('avatar', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
 
class Profile (models.Model):
    username = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    avatar = CloudinaryField('avatar', null=True, blank=True)
    address = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    region = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.user.last_name} Profile'
    
    def save_profile(self):
        self.save
        
    def delete_profile(self):
        self.delete()


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='prod')

    def __str__(self):
        return self.name
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
        
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(_('date of order'), auto_now_add=True)
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='order')

    def __str__(self):
        return self.name
    
    def save_order(self):
        self.save()

    def delete_order(self):
        self.delete()
        
               
