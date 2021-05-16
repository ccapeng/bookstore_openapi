from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
 
from book.models import Category
from book.serializers import CategorySerializer


def get_category(category):
    category_serializer = CategorySerializer(category) 
    return Response(category_serializer.data) 
 
def update_category(category, request):
    category_data = JSONParser().parse(request) 
    category_serializer = CategorySerializer(category, data=category_data) 
    if category_serializer.is_valid(): 
        category_serializer.save() 
        return Response(category_serializer.data) 
    return Response(
        category_serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
    ) 
 
def delete_category(category):
    category.delete() 
    return Response(
        {'message': 'Category was deleted successfully.'}, 
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, id):
    try: 
        category = Category.objects.get(pk=id) 
    except Category.DoesNotExist: 
        return Response(
            {'message': 'The category does not exist.'}, 
            status=status.HTTP_404_NOT_FOUND
        ) 
 
    if request.method == 'GET': 
        return get_category(category)
 
    elif request.method == 'PUT': 
        return update_category(category, request)
 
    elif request.method == 'DELETE': 
        return delete_category(category)