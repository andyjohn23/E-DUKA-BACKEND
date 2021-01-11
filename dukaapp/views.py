from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import viewsets,status,generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from django.http import HttpResponse, Http404
import json
from rest_framework import filters  
from rest_framework.generics import ListAPIView

# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSignupSerializer
    queryset = User.objects.all()
    
class SignupAPIView(generics.GenericAPIView):
    serializer_class = UserSignupSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSignupSerializer(user,context=self.get_serializer_context()).data,
            # "token": AuthToken.objects.create(user)[1]
        })

class LogoutAPIView(generics.CreateAPIView):
    serializer_class=LogoutSerializer
    permission_classes=(IsAuthenticated,)
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token=request.data.get('refresh_token')
        error_message={
            "error":"Token is invalid or expired"
        }
        success_message={
            "success":"Logout successfully"
        }        
        try:
            token=RefreshToken(token)
            token.blacklist()
        except TokenError as error:
            return Response(error_message,status=status.HTTP_400_BAD_REQUEST)
        return Response(success_message,status=status.HTTP_200_OK)

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)


    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        
class ShopViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing shop instances.
    """
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    
class ShopsViewSet(APIView):
    def get(self, request, format=None):      
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        permission_classes = [IsAuthenticated,IsMerchantOrAdmin]
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategorysViewSet(APIView):
    def get(self, request, format=None):      
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        permission_classes = [IsAuthenticated,IsMerchantOrAdmin]
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    serializer_class = Sub_CategorySerializer
    queryset = Sub_Category.objects.all()
    
class ProductViewSets(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductViewSet(APIView):
    def get(self, request, format=None):      
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        permission_classes = [IsAuthenticated,IsMerchantOrAdmin]
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(APIView):
    """
    Retrieve, update or delete product instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        permission_classes = [IsAuthenticated, IsMerchantOrAdmin]
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        permission_classes = [IsAuthenticated, IsMerchantOrAdmin]
        product = self.get_object(pk)
        ProductSerializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
class CommentsViewSet(APIView):
    def get(self, request, format=None):      
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        permission_classes = [IsAuthenticated,IsCustomerOrMerchantOrAdmin]
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentsDetail(APIView):
    """
    Retrieve, update or delete product instance.
    """
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        permission_classes = [IsAuthenticated, IsCustomerOrMerchantOrAdmin]
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrdersViewSet(APIView):
    def get(self, request, format=None):      
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        permission_classes = [IsAuthenticated,IsCustomerOrMerchantOrAdmin]
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ProductListAPIView(generics.ListAPIView):
#     serializer_class = ProductSerializer
#     # filter_backends = (filters.DjangoFilterBackend,)
#     # filter_fields=("department__name",)
    
#     def get_serializer_context(self, *args, **kwargs):
#         context =super(ProductListAPIView, self).get_serializer_context(*args, **kwargs)
#         context['request'] = self.request
#         return context

#     def get_queryset(self, *args, **kwargs):
#         requested_user = self.kwargs.get("email")
#         if requested_user: 
#             qs = Product.objects.filter(user__email=requested_user).order_by("date_added")
#         else:
#             my_following = self.request.user.profile.get_following()
#             qs1 = Product.objects.filter(user__in=my_following)
#             qs2 = Product.objects.filter(user=self.request.user)
#             qs = (qs1 | qs2).order_by("date_added")
#             print(self.request.GET)
#         query = self.request.GET.get("q", None)
#         if query is not None:
#             qs = qs.filter(
#                 Q(content__icontains=query) |
#                 Q(user__email__icontains=query)
#             )
#         return qs 

class ProductSubcategory(ListAPIView):
    serializer_class = ProductSerializer
    queryset= Product.objects.all()
    
    def get(self, request, category_id, *args, **kwargs): 
        sub_category = get_object_or_404(Sub_Category, pk=category)
        queryset = Product.objects.filter(sub_category=sub_category)
        
        if not queryset:
            message = {}
            return Response(message, status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset, many=True,
                                               context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

