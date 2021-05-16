from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
 
from book.models import Publisher
from book.serializers import PublisherSerializer


def get_publisher_list(request):
    publishers = Publisher.objects.all()
    name = request.query_params.get('name', None)
    if name is not None:
        publishers = publishers.filter(name__icontains=name)
    publishers_serializer = PublisherSerializer(publishers, many=True)
    return Response(publishers_serializer.data)

    
def create_publisher(request):
    publisher_data = JSONParser().parse(request)
    publisher_serializer = PublisherSerializer(data=publisher_data)
    if publisher_serializer.is_valid():
        publisher_serializer.save()
        return Response(publisher_serializer.data, status=status.HTTP_201_CREATED) 
    return Response(publisher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


def delete_publisher_list(request):
    count = Publisher.objects.all().delete()
    return Response(
        {'message': '{} publishers were deleted successfully.'.format(count[0])}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'POST', 'DELETE'])
def publisher_list(request):
    if request.method == 'GET':
        return get_publisher_list(request)
    elif request.method == 'POST':
        return create_publisher(request)
    elif request.method == 'DELETE':
        return delete_publisher_list(request)