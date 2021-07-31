from django.db import models

# Create your models here.


class MyModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Artist(MyModel):
    class Meta:
        db_table: 'record_label_artist'
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Prefer not to say')
    )
    first_name = models.CharField(max_length=255, unique=False)
    last_name = models.CharField(max_length=255, unique=False)
    name = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=10, choices=gender_options, unique=False)
    phone = models.CharField(max_length=15, unique=True)
    mail = models.CharField(max_length=255, unique=True)


class Album(MyModel):
    class Meta:
        db_table: 'record_label_album'
    title = models.CharField(max_length=255, unique=False)
    no_songs = models.IntegerField()


class Song(MyModel):
    class Meta:
        db_table: 'record_label_song'
    name = models.CharField(max_length=255, unique=False)
    id_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    id_album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField()


class Collaboration(MyModel):
    class Meta:
        db_table: 'record_label_collaboration'
        unique_together = (("id_song", "id_artist"),)
    id_song = models.ForeignKey(Song, on_delete=models.CASCADE)
    id_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Location(MyModel):
    class Meta:
        db_table: 'record_label_location'

    country = models.CharField(max_length=255, unique=False)
    city = models.CharField(max_length=255, unique=False)
    street = models.CharField(max_length=255, unique=False)
    name = models.CharField(max_length=255, unique=False)


class Concert(MyModel):
    class Meta:
        db_table: 'record_label_concert'

    id_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()


class Contract(MyModel):
    class Meta:
        db_table: 'record_label_contract'
        unique_together = (("id_artist", "id_concert"),)

    id_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    id_concert = models.ForeignKey(Concert, on_delete=models.CASCADE)