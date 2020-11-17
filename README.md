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
	- React hook context project [https://github.com/ccapeng/bookstore-context](https://github.com/ccapeng/bookstore-context)
	- React redux typescript project [https://github.com/ccapeng/bookstore-ts-redux](https://github.com/ccapeng/bookstore-ts-redux)
	- React redux form project [https://github.com/ccapeng/bookstore-redux-form](https://github.com/ccapeng/bookstore-redux-form)
  
- To expose api, 
  - Enter http://127.0.0.1:8001 to see 4 api end point.
    ```
    "api/category": "http://127.0.0.1:8001/api/category/",
    "api/publisher": "http://127.0.0.1:8001/api/publisher/",
    "api/author": "http://127.0.0.1:8001/api/author/",
    "api/book": "http://127.0.0.1:8001/api/book/"
    ```
  - and to download, enter http://127.0.0.1:8001/swagger.yaml