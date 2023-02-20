from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from .requests import get_data_from_gutendex

# Create your views here.


class BookViewset(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    if Book.objects.count() == 0:
        data = get_data_from_gutendex()
        for book in data:
            exists = Book.objects.filter(book_id=book['id']).exists()
            if not exists:
                Book.objects.create(
                    book_id=book['id'],
                    title=book['title'],
                    author=book['authors'][0]['name'],
                    language=book['languages'][0],
                    copyright=book['copyright']
                )

    serializer_class = BookSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = Book.objects.all()
        language = self.request.query_params.get('language')
        if language is not None:
            queryset = queryset.filter(language=language)

        return queryset
