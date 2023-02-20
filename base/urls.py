from rest_framework.routers import DefaultRouter
from django.urls import path
from .import views


router = DefaultRouter()
router.register('books', views.BookViewset, basename='books')

urlpatterns = router.urls
