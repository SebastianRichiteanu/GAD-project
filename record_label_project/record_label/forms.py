from django import forms

from .models import *


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "title",
            "no_songs",
            "publish_date"
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
            "artist",
            "album",
            "publish_date"
        ]


class CollaborationForm(forms.ModelForm):
    class Meta:
        model = Collaboration
        fields = [
            "song",
            "artist"
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
            "location",
            "concert_date"
        ]


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "artist",
            "concert",
            "salary"
        ]
