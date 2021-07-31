"""record_label_project URL Configuration

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
from django.contrib import admin
from django.urls import path
from record_label.views import homepage
from record_label.particural_views.albums import create_album, list_albums, view_album, update_album, delete_album

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),

    path('albums', list_albums),
    path('albums/create', create_album),
    path('albums/<id>', view_album),
    path('albums/<id>/update', update_album),
    path('albums/<id>/delete', delete_album)
]
