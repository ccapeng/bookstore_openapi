# from rest_framework import viewsets, permissions
from collections import OrderedDict
#from django.shortcuts import get_object_or_404

#from rest_framework import viewsets, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import \
    CategorySerializer, \
    PublisherSerializer, \
    AuthorSerializer, \
    BookSerializer
from .models import Category, Publisher, Author, Book
# from django.core.exceptions import PermissionDenied


class CategoryViewSet(viewsets.ModelViewSet):
    """ Category ViewSet """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PublisherViewSet(viewsets.ModelViewSet):
    """ Publisher ViewSet """
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    """ Author ViewSet """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    """ Book ViewSet """
    serializer_class = BookSerializer
    queryset = Book.objects.all()