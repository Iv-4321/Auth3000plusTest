from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class PaginationMovies(PageNumberPagination):
    page_size = 6
    max_page_size = 100


    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


# from django_filters import rest_framework as filters
#
# from .models import Book
#
#
# class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
#     pass
#
#
# class BookFilter(filters.FilterSet):
#     name = CharFilterInFilter(field_name='name', lookup_expr='in')
#     author = CharFilterInFilter(field_name='author', lookup_expr='in')
#
#     class Meta:
#         model = Book
#         fields = ['name', 'author']
