from django.contrib import admin
from django.urls import path, include  # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('mis.urls')),  # Include URLs from the 'mis' app
]
