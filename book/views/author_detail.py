from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from book.models import Author
from book.serializers import AuthorSerializer
from rest_framework.decorators import api_view


def get_author(author):
    author_serializer = AuthorSerializer(author) 
    return JsonResponse(author_serializer.data) 
 
def update_author(author, request):
    author_data = JSONParser().parse(request) 
    author_serializer = AuthorSerializer(author, data=author_data) 
    if author_serializer.is_valid(): 
        author_serializer.save() 
        return JsonResponse(author_serializer.data) 
    return JsonResponse(
        author_serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
    ) 
 
def delete_author(author):
    author.delete() 
    return JsonResponse(
        {'message': 'Author was deleted successfully.'}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, id):
    try: 
        author = Author.objects.get(pk=id) 
    except Author.DoesNotExist: 
        return JsonResponse(
            {'message': 'The author does not exist.'}, 
            status=status.HTTP_404_NOT_FOUND
        ) 
 
    if request.method == 'GET': 
        return get_author(author)
 
    elif request.method == 'PUT': 
        return update_author(author, request)
 
    elif request.method == 'DELETE': 
        return delete_author(author)        
