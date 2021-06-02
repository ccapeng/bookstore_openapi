from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __repr__(self):
        return f"<Category {self.name}>"


class Publisher(models.Model):
    name = models.CharField(max_length=32, unique=True)
    def __repr__(self):
        return f"<Publisher {self.name}>"


class Author(models.Model):
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)

    def __repr__(self):
        return f"<Author {self.last_name} {self.first_name}>"

    @property
    def name(self):
        return self.last_name + " " + self.first_name


class BookManager(models.Manager):

    def get_list_detail(self):
        qs = super().get_queryset()
        return qs.select_related('category', 'publisher', 'author')


class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, 
        null=True, 
        on_delete=models.SET_NULL,
        related_name="category"
    )
    publisher = models.ForeignKey(
        Publisher, 
        null=True, 
        on_delete=models.SET_NULL,
        related_name="publisher"
    )
    author = models.ForeignKey(
        Author, 
        null=True, 
        on_delete=models.SET_NULL,
        related_name="author"
    )

    objects = BookManager()

    def __repr__(self):
        return f"<Book {self.title}>"
