from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
    # , BookCreateView

router = DefaultRouter()
router.register(r'books', BookViewSet)
# router.register(r'upload', BookCreateView)

urlpatterns = [
    path("", include(router.urls)),

]