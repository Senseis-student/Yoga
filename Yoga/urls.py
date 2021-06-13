from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('program.urls')),
    path('location', include('branches.urls')),
    path('form', include('form.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)