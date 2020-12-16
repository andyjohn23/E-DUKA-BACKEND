from __future__ import unicode_literals

from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField


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
    

     def save_category(self):
            self.save()

    def delete_category(self):
        self.delete()

class Sub-Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='sub-category')

    def __str__(self):
        return self.name
    
     def save_sub-category(self):
            self.save()

    def delete_sub-category(self):
        self.delete()


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

    def delete_product(self):
        self.delete()

from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager
from django.contrib.auth.base_user import BaseUserManager

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
        
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('active'), default=True)
    is_active = models.BooleanField(_('active'), default=True)
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
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    status = models.BooleanField()
    image = CloudinaryField('Profile pic', default = 'profile.jpg')
    
    def __str__(self):
        return f'{self.user.last_name} Profile'
    
    def save_profile(self):
        self.save
        
    def delete_profile(self):
        self.delete()

class Role(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_admin = models.BooleanField( default=False)
    is_merchant = models.BooleanField( default=False)
    is_customer = models.BooleanField( default=False)
    
    def __str__(self):
        return f'{self.user.last_name} Profile'
    
    def save_profile(self):
        self.save
        
    def delete_profile(self):
        self.delete()
        
               
