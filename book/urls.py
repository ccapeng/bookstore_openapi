from rest_framework import routers
from django.urls import path

from book.views.category_list import category_list
from book.views.category_detail import category_detail
from book.views.publisher_list import publisher_list
from book.views.publisher_detail import publisher_detail
from book.views.author_list import author_list
from book.views.author_detail import author_detail
from book.views.book_list import book_list
from book.views.book_detail import book_detail

urlpatterns = [ 
    path('api/categories', category_list),
    path('api/categories/<int:id>', category_detail),

    path('api/publishers', publisher_list),
    path('api/publishers/<int:id>', publisher_detail),

    path('api/authors', author_list),
    path('api/authors/<int:id>', author_detail),

    path('api/books', book_list),
    path('api/books/<int:id>', book_detail),
]