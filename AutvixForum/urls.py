"""AutvixForum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pathlib import Path
from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings
from Forum import views

urlpatterns = [
    # Principal pages
    path('', views.home),
    path('posts/<int:post_id>', views.post),
    path('newPost/', views.newPost, name='new-post'),
    path('keyWords/', views.keyWords, name='key-words'),
    path('search/<str:kw>', views.search, name='search'),

    # Auxiliary pages
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    # Auth pages
    path('accounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
