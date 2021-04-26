from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from book.models import Author
from book.serializers import AuthorSerializer
from rest_framework.decorators import api_view


def get_author_list(request):
    authors = Author.objects.all()
    last_name = request.query_params.get('last_name', None)
    if last_name is not None:
        authors = authors.filter(last_name__icontains=last_name)
    first_name = request.query_params.get('first_name', None)
    if first_name is not None:
        authors = authors.filter(last_name__icontains=first_name)
    authors_serializer = AuthorSerializer(authors, many=True)
    return JsonResponse(authors_serializer.data, safe=False)

    
def create_author(request):
    author_data = JSONParser().parse(request)
    author_serializer = AuthorSerializer(data=author_data)
    if author_serializer.is_valid():
        author_serializer.save()
        return JsonResponse(author_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


def delete_author_list(request):
    count = Author.objects.all().delete()
    return JsonResponse(
        {'message': '{} authors were deleted successfully.'.format(count[0])}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'POST', 'DELETE'])
def author_list(request):
    print("request.method", request.method)
    if request.method == 'GET':
        return get_author_list(request)
    elif request.method == 'POST':
        return create_author(request)
    elif request.method == 'DELETE':
        return delete_author_list(request)
