from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from book.models import Book
from book.serializers import BookDetailSerializer
from rest_framework.decorators import api_view


def get_book_list(request):
    books = Book.objects.all()
    title = request.query_params.get('title', None)
    if title is not None:
        books = books.filter(title__icontains=title)
    books_serializer = BookDetailSerializer(books, many=True)
    return JsonResponse(books_serializer.data, safe=False)

    
def create_book(request):
    book_data = JSONParser().parse(request)
    book_serializer = BookSerializer(data=book_data)
    if book_serializer.is_valid():
        book_serializer.save()
        return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


def delete_book_list(request):
    count = Book.objects.all().delete()
    return JsonResponse(
        {'message': '{} books were deleted successfully.'.format(count[0])}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'POST', 'DELETE'])
def book_list(request):
    print("request.method", request.method)
    if request.method == 'GET':
        return get_book_list(request)
    elif request.method == 'POST':
        return create_book(request)
    elif request.method == 'DELETE':
        return delete_book_list(request)
