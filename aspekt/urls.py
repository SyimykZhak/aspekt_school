"""aspekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include 
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from django.views.static import serve as mediaserve
from django.urls  import re_path


urlpatterns = [
    path('', include("core.urls")),
    path('as-admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('courses/', include("courses.urls")),
    path('news/', include("news.urls")),
)

handler404 = "core.views.handle_not_found"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns +=[
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
        mediaserve, {'document_root': settings.MEDIA_ROOT}),
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
        mediaserve, {'document_root': settings.STATIC_ROOT}),
        ]