from rest_framework.response import Response
from rest_framework import generics
from . models import Book
from . serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# RetrieveAPIView - used for read-only endpoints to represent a single model instance.
# https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview
class BookView(generics.RetrieveAPIView):

    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
