from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from student_management_system import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_management_app.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
