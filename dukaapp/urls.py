from rest_framework.routers import DefaultRouter
from django.urls import path,re_path,include
from . import views
from .views import *
from knox import views as knox_views
# from .views import LoginAPI
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()

urlpatterns =[
    path('api/v1/', include(router.urls)),

] 

