from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # filterset_fields = ['prise']
    search_fields = ['name', 'author']

    def perform_create(self, serializer):
        # parserPdf()
        serializer.save()

    def post(self, ):
        pass
