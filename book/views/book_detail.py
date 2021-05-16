from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from any_case import converts_keys
from book.models import Book, Category, Publisher, Author
from book.serializers import BookDetailSerializer, BookSerializer


def get_book(book):
    book_serializer = BookSerializer(book) 
    return Response(book_serializer.data) 
 
def update_book(book, request):
    data = JSONParser().parse(request)
    # convert keys from camelCase to snake_case
    data = converts_keys(data, case='snake')
    serializer = BookDetailSerializer(book, data=data)
    # print("book_serializer:", book_serializer)
    if serializer.is_valid(): 
        print("is valid")
        category, publisher, author = None, None, None
        category_id = data.get("category_id", None)
        publisher_id =  data.get("publisher_id", None)
        author_id =  data.get("author_id", None)
        if category_id:
            category = Category.objects.get(pk=category_id) 
        if publisher_id:
            publisher = Publisher.objects.get(pk=publisher_id) 
        if author_id:
            author = Author.objects.get(pk=author_id) 
        serializer.save(
            category = category,
            publisher =  publisher,
            author =  author,
        ) 
        print("book_serializer.data:", serializer.data)
        return Response(serializer.data)

    print("not valid")
    return Response(
        serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
    ) 

    # book_serializer.is_valid(raise_exception=True)
    # print("is valid")
    # category, publish, author = None, None, None
    # category_id = book_data.get("category_id", None)
    # publisher_id =  book_data.get("publisher_id", None)
    # author_id =  book_data.get("author_id", None)
    # if category_id:
    #     category = Category.objects.get(pk=category_id) 
    # if publisher_id:
    #     publisher = Publisher.objects.get(pk=publisher_id) 
    # if author_id:
    #     author = Author.objects.get(pk=author_id) 
    # book_serializer.save(
    #     category = category,
    #     publisher =  publisher,
    #     author =  author,
    # ) 
    # print("book_serializer.data:", book_serializer.data)
    # return Response(book_serializer.data)

 
def delete_book(book):
    book.delete() 
    return Response(
        {'message': 'Book was deleted successfully.'}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, id):
    try: 
        book = Book.objects.get(pk=id) 
    except Book.DoesNotExist: 
        return Response(
            {'message': 'The book does not exist.'}, 
            status=status.HTTP_404_NOT_FOUND
        ) 
 
    if request.method == 'GET': 
        return get_book(book)
 
    elif request.method == 'PUT': 
        return update_book(book, request)
 
    elif request.method == 'DELETE': 
        return delete_book(book)