import os
from django.urls import path
from bookstore_openapi import settings

# function based view
if settings.API_VIEW == 'function':
    print("use function based view")
    from book.views.category_list import category_list
    from book.views.category_detail import category_detail
    from book.views.publisher_list import publisher_list
    from book.views.publisher_detail import publisher_detail
    from book.views.author_list import author_list
    from book.views.author_detail import author_detail
    from book.views.book_list import book_list
    from book.views.book_detail import book_detail

    urlpatterns = [ 
        path('api/categories', category_list, name="category_list"),
        path('api/categories/<int:id>', category_detail, name="category_detail"),
        path('api/publishers', publisher_list, name="publisher_list"),
        path('api/publishers/<int:id>', publisher_detail, name="publisher_detail"),
        path('api/authors', author_list, name="author_list"),
        path('api/authors/<int:id>', author_detail, name="author_detail"),
        path('api/books', book_list, name="book_list"),
        path('api/books/<int:id>', book_detail, name="book_detail"),
    ]

#class based view
else:
    print("use class based view")
    from book import api

    urlpatterns = [ 
        path('api/categories', api.CategoryList.as_view()),
        path('api/categories/<int:pk>', api.CategoryDetail.as_view()),
        path('api/publishers', api.PublisherList.as_view()),
        path('api/publishers/<int:pk>', api.PublisherDetail.as_view()),
        path('api/authors', api.AuthorList.as_view()),
        path('api/authors/<int:pk>', api.AuthorDetail.as_view()),
        path('api/books', api.BookList.as_view()),
        path('api/books/<int:pk>', api.BookDetail.as_view()),
    ]