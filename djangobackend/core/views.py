from django.core.files.uploadedfile import UploadedFile
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # filterset_fields = ['prise']
    search_fields = ['name', 'author']

    def perform_create(self, UploadedFile):
        # parserPdf()
        print("name")

        test = UploadedFile.get('pdf')
        # test = request.data.get('pdf')
        print(test)

        return Response('test', status=status.HTTP_201_CREATED)


# class CreateCategory(APIView):
#
#     def post(self, request, format=None):
#         # parserPdf()
#         print("test")
#
#         test = request.data.get("test")
#         print(test)
#
#         return Response('test', status=status.HTTP_201_CREATED)

# class CreateCategory(APIView):
#
#     def perform_create(self, serializer):
#         # parserPdf()
#         print('test', )
#         serializer.save()
#         return Response('test', status=status.HTTP_201_CREATED)
