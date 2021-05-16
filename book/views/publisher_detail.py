
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
 
from book.models import Publisher
from book.serializers import PublisherSerializer


def get_publisher(publisher):
    publisher_serializer = PublisherSerializer(publisher) 
    return Response(publisher_serializer.data) 
 
def update_publisher(publisher, request):
    publisher_data = JSONParser().parse(request) 
    publisher_serializer = PublisherSerializer(publisher, data=publisher_data) 
    if publisher_serializer.is_valid(): 
        publisher_serializer.save() 
        return Response(publisher_serializer.data) 
    return Response(
        publisher_serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
    ) 
 
def delete_publisher(publisher):
    publisher.delete() 
    return Response(
        {'message': 'Publisher was deleted successfully.'}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'PUT', 'DELETE'])
def publisher_detail(request, id):
    try: 
        publisher = Publisher.objects.get(pk=id) 
    except Publisher.DoesNotExist: 
        return Response(
            {'message': 'The publisher does not exist.'}, 
            status=status.HTTP_404_NOT_FOUND
        ) 
 
    if request.method == 'GET': 
        return get_publisher(publisher)
 
    elif request.method == 'PUT': 
        return update_publisher(publisher, request)
 
    elif request.method == 'DELETE': 
        return delete_publisher(publisher)        
