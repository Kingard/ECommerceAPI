from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category,related_name='books',on_delete=models.CASCADE)
    author = models.CharField(max_length=70,default='author')
    isbn = models.CharField(max_length=20)
    pages = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField() # Quantity
    description = models.TextField()
    image_url = models.URLField()
    created_by = models.ForeignKey('auth.User',related_name='books',on_delete=models.CASCADE)
    status = models.BooleanField(default=True) #is the book available, y/n
    date_created = models.DateField(auto_now_add=True)

    class Meta: # This is simply an inner-class that helps change the behaviour of the models, e.g ordering
        ordering = ['-date_created'] 


    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.URLField()
    created_by = models.ForeignKey('auth.User',related_name='products',on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.product_tag+' '+self.name