from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import viewsets,status,generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from django.http import HttpResponse, Http404

# Create your views here.




class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSignupSerializer
    queryset = User.objects.a
