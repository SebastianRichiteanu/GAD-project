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
from record_label.particural_views.artists import create_artist, list_artists, view_artist, update_artist, delete_artist
from record_label.particural_views.songs import create_song, list_songs, view_song, update_song, delete_song
from record_label.particural_views.collaborations import create_collaboration, list_collaborations, \
    view_collaboration, update_collaboration, delete_collaboration
from record_label.particural_views.locations import create_location, list_locations, view_location, \
    update_location, delete_location
from record_label.particural_views.concerts import create_concert, list_concerts, view_concert, update_concert, \
    delete_concert
from record_label.particural_views.contracts import create_contract, list_contracts, view_contract, update_contract, \
    delete_contract


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),

    path('albums', list_albums),
    path('albums/create', create_album),
    path('albums/<id>', view_album),
    path('albums/<id>/update', update_album),
    path('albums/<id>/delete', delete_album),

    path('artists', list_artists),
    path('artists/create', create_artist),
    path('artists/<id>', view_artist),
    path('artists/<id>/update', update_artist),
    path('artists/<id>/delete', delete_artist),

    path('songs', list_songs),
    path('songs/create', create_song),
    path('songs/<id>', view_song),
    path('songs/<id>/update', update_song),
    path('songs/<id>/delete', delete_song),

    path('collaborations', list_collaborations),
    path('collaborations/create', create_collaboration),
    path('collaborations/<id>', view_collaboration),
    path('collaborations/<id>/update', update_collaboration),
    path('collaborations/<id>/delete', delete_collaboration),

    path('locations', list_locations),
    path('locations/create', create_location),
    path('locations/<id>', view_location),
    path('locations/<id>/update', update_location),
    path('locations/<id>/delete', delete_location),

    path('concerts', list_concerts),
    path('concerts/create', create_concert),
    path('concerts/<id>', view_concert),
    path('concerts/<id>/update', update_concert),
    path('concerts/<id>/delete', delete_concert),

    path('contracts', list_contracts),
    path('contracts/create', create_contract),
    path('contracts/<id>', view_contract),
    path('contracts/<id>/update', update_contract),
    path('contracts/<id>/delete', delete_contract),

]
