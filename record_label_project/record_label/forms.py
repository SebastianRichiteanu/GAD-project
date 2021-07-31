from django import forms

from .models import *


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "title",
            "no_songs"
        ]


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            "first_name",
            "last_name",
            "name",
            "gender",
            "phone",
            "mail"
        ]


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            "title",
            "id_artist",
            "id_album",
            "publish_date"
        ]


class CollaborationForm(forms.ModelForm):
    class Meta:
        model = Collaboration
        fields = [
            "id_song",
            "id_artist"
        ]


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            "country",
            "city",
            "street",
            "name"
        ]


class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = [
            "id_location",
            "concert_date"
        ]


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "id_artist",
            "id_concert",
            "salary"
        ]
