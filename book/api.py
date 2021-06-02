from rest_framework import generics
from rest_framework import mixins

from book.serializers import \
    CategorySerializer, \
    PublisherSerializer, \
    AuthorSerializer, \
    BookListDetailSerializer, \
    BookSerializer
from book.models import Category, Publisher, Author, Book

# For more correct documentation, 
# use mixin class instead of generic class.

# class CategoryList(generics.ListCreateAPIView):
#     """
#     List all categories, or create a new category.
#     """
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
class CategoryList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        """
        List all categories.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create a new category.
        """
        return self.create(request, *args, **kwargs)

# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update or delete a category instance.
#     """
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
class CategoryDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        """
        Get a category instance.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Update a category.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete a category.
        """
        return self.destroy(request, *args, **kwargs)


# class PublisherList(generics.ListCreateAPIView):
#     """
#     List all publisers, or create a new publisher.
#     """
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
class PublisherList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get(self, request, *args, **kwargs):
        """
        List all publishers.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create a new publisher.
        """
        return self.create(request, *args, **kwargs)


# class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update or delete a category instance.
#     """
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer      
class PublisherDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get(self, request, *args, **kwargs):
        """
        Get a publisher instance.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Update a publisher.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete a publisher.
        """
        return self.destroy(request, *args, **kwargs)


# class AuthorList(generics.ListCreateAPIView):
#     """
#     List all authors, or create a new author.
#     """
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
class AuthorList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        """
        List all authors.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create a new author.
        """
        return self.create(request, *args, **kwargs)


# class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update or delete a category instance.
#     """
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer      
class AuthorDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        """
        Get an author instance.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Update an author.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete an author.
        """
        return self.destroy(request, *args, **kwargs)

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

    # queryset = Book.objects \
    #     .select_related("category","publisher","author") \
    #     .all() 
    queryset = Book.objects.get_list_detail()
    serializer_class = BookListDetailSerializer

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
        Update a book.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete a book.
        """
        return self.destroy(request, *args, **kwargs)