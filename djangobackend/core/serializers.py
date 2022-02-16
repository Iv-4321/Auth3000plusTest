from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    # def post(self, ):


    class Meta:
        model = Book
        fields = '__all__'



