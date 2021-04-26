from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from book.models import Book
from book.serializers import BookSerializer
from rest_framework.decorators import api_view


def get_book(book):
    book_serializer = BookSerializer(book) 
    return JsonResponse(book_serializer.data) 
 
def update_book(book, request):
    book_data = JSONParser().parse(request) 
    book_serializer = BookSerializer(book, data=book_data) 
    if book_serializer.is_valid(): 
        book_serializer.save() 
        return JsonResponse(book_serializer.data) 
    return JsonResponse(
        book_serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
    ) 
 
def delete_book(book):
    book.delete() 
    return JsonResponse(
        {'message': 'Book was deleted successfully.'}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, id):
    try: 
        book = Book.objects.get(pk=id) 
    except Book.DoesNotExist: 
        return JsonResponse(
            {'message': 'The book does not exist.'}, 
            status=status.HTTP_404_NOT_FOUND
        ) 
 
    if request.method == 'GET': 
        return get_book(book)
 
    elif request.method == 'PUT': 
        return update_book(book, request)
 
    elif request.method == 'DELETE': 
        return delete_book(book)        
