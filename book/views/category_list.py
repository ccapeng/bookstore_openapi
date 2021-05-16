from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
 
from book.models import Category
from book.serializers import CategorySerializer

def get_category_list(request):
    categories = Category.objects.all()
    name = request.query_params.get('name', None)
    if name is not None:
        categories = categories.filter(name__icontains=name)
    categories_serializer = CategorySerializer(categories, many=True)
    return Response(categories_serializer.data)

    
def create_category(request):
    category_data = JSONParser().parse(request)
    category_serializer = CategorySerializer(data=category_data)
    if category_serializer.is_valid():
        category_serializer.save()
        return Response(category_serializer.data, status=status.HTTP_201_CREATED) 
    return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_category_list(request):
    count = Category.objects.all().delete()
    return Response(
        {'message': '{} categories were deleted successfully.'.format(count[0])}, 
        status=status.HTTP_204_NO_CONTENT
    )

@api_view(['GET', 'POST', 'DELETE'])
def category_list(request):
    if request.method == 'GET':
        return get_category_list(request)
    elif request.method == 'POST':
        return create_category(request)
    elif request.method == 'DELETE':
        return delete_category_list(request)
