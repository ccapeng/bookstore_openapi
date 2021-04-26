from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from book.models import Publisher
from book.serializers import PublisherSerializer
from rest_framework.decorators import api_view


def get_publisher(publisher):
    publisher_serializer = PublisherSerializer(publisher) 
    return JsonResponse(publisher_serializer.data) 
 
def update_publisher(publisher, request):
    publisher_data = JSONParser().parse(request) 
    publisher_serializer = PublisherSerializer(publisher, data=publisher_data) 
    if publisher_serializer.is_valid(): 
        publisher_serializer.save() 
        return JsonResponse(publisher_serializer.data) 
    return JsonResponse(
        publisher_serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
    ) 
 
def delete_publisher(publisher):
    publisher.delete() 
    return JsonResponse(
        {'message': 'Publisher was deleted successfully.'}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'PUT', 'DELETE'])
def publisher_detail(request, id):
    try: 
        publisher = Publisher.objects.get(pk=id) 
    except Publisher.DoesNotExist: 
        return JsonResponse(
            {'message': 'The publisher does not exist.'}, 
            status=status.HTTP_404_NOT_FOUND
        ) 
 
    if request.method == 'GET': 
        return get_publisher(publisher)
 
    elif request.method == 'PUT': 
        return update_publisher(publisher, request)
 
    elif request.method == 'DELETE': 
        return delete_publisher(publisher)        
