from django.contrib import admin
from .models import Artist, Album, Song, Collaboration, Location, Concert, Contract


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'first_name', 'last_name')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date', 'get_no_songs')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'album', 'publish_date')


@admin.register(Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    list_display = ('id', 'song', 'artist')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_address')


@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'concert_date')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'concert', 'salary')
