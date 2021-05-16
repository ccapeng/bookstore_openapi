from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from any_case import converts_keys
from book.models import Author
from book.serializers import AuthorSerializer


def get_author_list(request):
    authors = Author.objects.all()
    last_name = request.query_params.get('last_name', None)
    if last_name is not None:
        authors = authors.filter(last_name__icontains=last_name)
    first_name = request.query_params.get('first_name', None)
    if first_name is not None:
        authors = authors.filter(last_name__icontains=first_name)
    authors_serializer = AuthorSerializer(authors, many=True)
    return Response(authors_serializer.data)

    
def create_author(request):
    author_data = JSONParser().parse(request)
    # convert keys from camelCase to snake_case
    author_data = converts_keys(author_data, case='snake')
    author_serializer = AuthorSerializer(data=author_data)
    if author_serializer.is_valid():
        author_serializer.save()
        return Response(author_serializer.data, status=status.HTTP_201_CREATED) 
    return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


def delete_author_list(request):
    count = Author.objects.all().delete()
    return Response(
        {'message': '{} authors were deleted successfully.'.format(count[0])}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'POST', 'DELETE'])
def author_list(request):
    if request.method == 'GET':
        return get_author_list(request)
    elif request.method == 'POST':
        return create_author(request)
    elif request.method == 'DELETE':
        return delete_author_list(request)