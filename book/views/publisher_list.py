from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from book.models import Publisher
from book.serializers import PublisherSerializer
from rest_framework.decorators import api_view


def get_publisher_list(request):
    publishers = Publisher.objects.all()
    name = request.query_params.get('name', None)
    if name is not None:
        publishers = publishers.filter(name__icontains=name)
    publishers_serializer = PublisherSerializer(publishers, many=True)
    return JsonResponse(publishers_serializer.data, safe=False)

    
def create_publisher(request):
    publisher_data = JSONParser().parse(request)
    publisher_serializer = PublisherSerializer(data=publisher_data)
    if publisher_serializer.is_valid():
        publisher_serializer.save()
        return JsonResponse(publisher_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(publisher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


def delete_publisher_list(request):
    count = Publisher.objects.all().delete()
    return JsonResponse(
        {'message': '{} publishers were deleted successfully.'.format(count[0])}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'POST', 'DELETE'])
def publisher_list(request):
    print("request.method", request.method)
    if request.method == 'GET':
        return get_publisher_list(request)
    elif request.method == 'POST':
        return create_publisher(request)
    elif request.method == 'DELETE':
        return delete_publisher_list(request)
