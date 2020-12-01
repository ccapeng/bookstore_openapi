from django.urls import include, path, reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Publisher, Author, Book


class BookTests(APITestCase):

    category_name = "Comic"

    def setUp(self):
        Category.objects.create(name=self.category_name)

    def test_category_content(self):
        id=1
        category = Category.objects.get(pk=id)
        expected_object_name = f'{category.name}'
        self.assertEquals(expected_object_name, self.category_name)
        

    def test_category_list_view(self):
        category_list = Category.objects.all()
        category_size = category_list.count()
        self.assertEquals(category_size, 1)
        url = reverse_lazy('api:category-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
