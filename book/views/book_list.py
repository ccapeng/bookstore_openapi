from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from any_case import converts_keys
from book.models import Book, Category, Publisher, Author
from book.serializers import BookSerializer, BookDetailSerializer


def get_book_list(request):
    books = Book.objects \
        .select_related("category", "publisher", "author") \
        .all() 
    print(books.query)
    title = request.query_params.get('title', None)
    if title is not None:
        books = books.filter(title__icontains=title)
    books_serializer = BookDetailSerializer(books, many=True)
    return Response(books_serializer.data)

    
def create_book(request):
    data = JSONParser().parse(request)
    # convert keys from camelCase to snake_case
    data = converts_keys(data, case='snake')
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        category, publisher, author = None, None, None
        category_id = data.get("category_id", None)
        publisher_id = data.get("publisher_id", None)
        author_id = data.get("author_id", None)
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
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


def delete_book_list(request):
    count = Book.objects.all().delete()
    return Response(
        {'message': '{} books were deleted successfully.'.format(count[0])}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'POST', 'DELETE'])
def book_list(request):
    if request.method == 'GET':
        return get_book_list(request)
    elif request.method == 'POST':
        return create_book(request)
    elif request.method == 'DELETE':
        return delete_book_list(request)