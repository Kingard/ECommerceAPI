from django.urls import path
from .views import ProductList, ProductDetail, BookList, BookDetail, CategoryList, CategoryDetail

urlpatterns = [
    path('categories/',CategoryList.as_view(),name = 'categoryList'),
    path('categories/<int:pk>/',CategoryDetail.as_view(),name='singleCategory'),
    path('books/',BookList.as_view(),name='bookList'),
    path('books/<int:pk>/',BookDetail.as_view(),name='singleBook'),
    path('products/',ProductList.as_view(),name='productList'),
    path('products/<int:pk>/',ProductDetail.as_view(),name='singleProduct')
]
