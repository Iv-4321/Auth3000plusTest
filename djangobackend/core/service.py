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
