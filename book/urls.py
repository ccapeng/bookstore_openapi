from rest_framework import routers
from .api import CategoryViewSet, PublisherViewSet, AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register("api/categories", CategoryViewSet, "category")
router.register("api/publishers", PublisherViewSet, "publisher")
router.register("api/authors", AuthorViewSet, "author")
router.register("api/books", BookViewSet, "book")

app_name = 'api'
urlpatterns = router.urls
