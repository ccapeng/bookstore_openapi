# Bookstore

- This is django REST

- To download it, clone : https://github.com/ccapeng/bookstore_openapi.git

- To start backend,
	- Make sure `python` and `pip` installed.
	- Then cd to `bookstore_openapi` directory.
	- For the first time, create virtual environment  
		`python -m venv env`
	- Then start the virtual environment `.\env\Scripts\activate`
	- Also for the very first time, run `pip install -r requirements.txt`
	- To start server, 
    - Run `python manage.py runserver 0.0.0.:8001`
    - Or,
      - Run `env.bat`
      - Then `run.bat`
	- Should able to connect it in http://localhost:8001 or http://127.0.0.1:8001
			
- This backend server also serve for
	- React hook redux project [https://github.com/ccapeng/bookstore-hook-redux](https://github.com/ccapeng/bookstore-hook-redux)
  
- To expose api, 
  - Enter http://127.0.0.1:8001/docs

- Tech Details:
  - API end points differences:
    - Function based view:
        ```
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

        # function based view
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
        ```
    - Class based view:
        ```
        from django.urls import path
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
        ```
  - Keys conversion between python variable snake case and JSON key camel case.
    - In function based view, use `any-case` module for request parsing.
    - In class based view, use middleware `utils.api.renderers.CamelCaseJSONRenderer` to output camel case JSON.