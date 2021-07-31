from django import forms
from .models import Album, Artist


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

