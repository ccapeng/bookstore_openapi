from rest_framework import generics
from rest_framework import mixins

from book.serializers import \
    CategorySerializer, \
    PublisherSerializer, \
    AuthorSerializer, \
    BookDetailSerializer, \
    BookSerializer
from book.models import Category, Publisher, Author, Book

class CategoryList(generics.ListCreateAPIView):
    """
    List all categories, or create a new category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a category instance.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PublisherList(generics.ListCreateAPIView):
    """
    List all publisers, or create a new publisher.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a category instance.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer      


class AuthorList(generics.ListCreateAPIView):
    """
    List all authors, or create a new author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a category instance.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer      


# class BookList(generics.ListCreateAPIView):
#     """
#     List all authors, or create a new book.
#     """
#     queryset = Book.objects \
#        .select_related("category","publisher","author") \
#        .all() 
#     serializer_class = BookDetailSerializer


# Use class view instead of generic class view
# 1. For better handle mutiple table data join.
# 2. Better document for open api.
class BookList( 
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

    queryset = Book.objects \
        .select_related("category","publisher","author") \
        .all() 
    serializer_class = BookDetailSerializer

    def get(self, request, *args, **kwargs):
        """
        List all books.
        """
        results = self.list(request, *args, **kwargs)
        # check sql in here. Make sure table join is happening.
        # print(*connection.queries, sep="\n")
        return results

    def post(self, request, *args, **kwargs):
        """
        Create a book instance.
        """
        return self.create(request, *args, **kwargs)


# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update or delete a book instance.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        """
        Get a book instance.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        update a book.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete a book.
        """
        return self.destroy(request, *args, **kwargs)