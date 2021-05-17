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

- The hard nut to crack:
  - API end point differences:
    - End point issue in Router
        ```
        router = routers.DefaultRouter()
        router.register("api/categories", CategoryViewSet, "category")
        ...
        In this kind url configuration, the end point is 
        `https://127.0.0.1/api/categories/`
        not
        `https://127.0.0.1/api/categories`
        The difference is at the end slash.  
        In general REST APIs practice, I prefer no end slash for listing.  
        In order to do that, `urlpatterns` is applied.
        ```
        urlpatterns = [ 
            path('api/categories', category_list, name="category_list"),
            path('api/categories/<int:id>', category_detail, name="category_detail"),
            ...
        ]
        ```

  - JSON naming conversion between snake case and camel case 
    - Use `any-case` module for request parsing.
    - Use middleware `utils.api.renderers.CamelCaseJSONRenderer` to output camel case JSON.