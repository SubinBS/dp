from django.urls import path, include
from . import views
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # Include the router's URLs for the API endpoints
    path('api/', include(router.urls)),  # Use 'api/' or another prefix as needed

    # Define additional URL patterns for non-API views
    path('', views.home, name='home'),  # Add this line for the root URL
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/update/<int:id>/', views.book_update, name='book_update'),
    path('books/delete/<int:id>/', views.book_delete, name='book_delete'),
]
