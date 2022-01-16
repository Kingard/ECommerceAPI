from django.db.models import fields
from rest_framework import serializers
from .models import Category,Book,Product
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ('id','first_name','last_name','email','username','password')

        def validate(self,args):
            email = args.get('email',None)
            username = args.get('username',None)
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({'email':('user already exists')})
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError({'username':('username already exists')})

            return super().validate(args)

        def create(self,validated_data):
            return User.objects.create_user(**validated_data)

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

#         return user
    

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