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


# user_profile = ProfileAPI.as_view({
#     'get': 'list',
#     'post': 'create'
# })


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profile', ProfileViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'sub_categories', SubCategoryViewSet)
# router.register(r'products', ProductViewSets)
router.register(r'orders', OrdersViewSet, basename='orders')
# router.register(r'comments', CommentViewSet)



urlpatterns = [
    path('auth/signup/', SignupAPIView.as_view(), name='user_signup'),
    path('profile1/', views.ProfileList.as_view(),name='profiles'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',views.LogoutAPIView.as_view(),name='logout'),
    # path('profile/<pk>/',views.ProfileList.as_view()),
    path('', include(router.urls)),
    path('products/', views.ProductViewSet.as_view(),name='products'),
    path('products/<int:pk>/', views.ProductDetail.as_view(),name='productdetails'),
    path('comments/', views.CommentsViewSet.as_view(),name='comments'),
    path('comments/<int:pk>/', views.CommentsDetail.as_view()),
    # path('orders/', views.OrdersViewSet.as_view()),
    path('categories/', views.CategorysViewSet.as_view()),
    path('shops/', views.ShopsViewSet.as_view()),
    path('filter_sub_category/<int:category_id>/', views.ProductSubcategory.as_view()),
    path('category_filter/<int:category_id>/', views.SubcategoryCategory.as_view()),
    path('filter_category/<int:category_id>/', views.ProductCategory.as_view()),
    path('search/', views.ProductSearchApiView.as_view()),
    # path('user/', views.UserList.as_view()),
]