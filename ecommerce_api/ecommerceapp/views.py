from ecommerceapp.models import Category
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import CategorySerializer,BookSerializer,ProductSerializer, RegistrationSerializer, UserSerializer
from .models import Category, Book, Product
from django.contrib.auth.models import User
from rest_framework import permissions ,status, serializers
from rest_framework.response import Response
from knox.models import AuthToken
import uuid


# Create your views here.
class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'RequestId':str(uuid.uuid4()),
                'Message': 'User created successfully',
                 'User': serializer.data}, status=status.HTTP_201_CREATED
                )
        return Response({'errors':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer