from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *
from django.contrib.auth.views import LoginView, LogoutView 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Users
user_signup = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'sub_categories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'comments', CommentViewSet)



urlpatterns = [
    path('auth/signup/', user_signup, name='user_signup'),
    path('api/adminprofile/', views.ProfileList.as_view(),name='adminprofiles'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',views.LogoutAPIView.as_view(),name='logout'),
    path('api/v1/profile/<pk>/',views.ProfileList.as_view()),
    path('api/v1/', include(router.urls)),
    
]