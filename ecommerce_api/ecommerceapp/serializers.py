from django.db.models import fields
from rest_framework import serializers
from .models import Category,Book,Product
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )

class BookSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'category',
            'author',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'image_url',
            'created_by',
            'status',
            'date_created'

        )

class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Product
        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'image_url',
            'created_by',
            'status',
            'date_created'

        )

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True,queryset=Book.objects.all())
    products = serializers.PrimaryKeyRelatedField(many=True,queryset=Product.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'books',
            'products'
        )