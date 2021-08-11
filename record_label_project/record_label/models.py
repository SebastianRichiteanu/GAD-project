from django.db import models


class MyModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Artist(MyModel):
    class Meta:
        db_table: 'artists'
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

    def __str__(self):
        return self.name


class Album(MyModel):
    class Meta:
        db_table: 'albums'
    title = models.CharField(max_length=255, unique=False)
    no_songs = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Song(MyModel):
    class Meta:
        db_table: 'songs'
    title = models.CharField(max_length=255, unique=False)
    id_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    id_album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank = True)
    publish_date = models.DateField()

    def __str__(self):
        return self.title


class Collaboration(MyModel):
    class Meta:
        db_table: 'collaborations'
        unique_together = (("id_song", "id_artist"),)
    id_song = models.ForeignKey(Song, on_delete=models.CASCADE)
    id_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.id_song)} {str(self.id_artist)}"


class Location(MyModel):
    class Meta:
        db_table: 'locations'

    country = models.CharField(max_length=255, unique=False)
    city = models.CharField(max_length=255, unique=False)
    street = models.CharField(max_length=255, unique=False)
    name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return f"{self.name}: {self.country}, {self.city}"


class Concert(MyModel):
    class Meta:
        db_table: 'concerts'

    id_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    concert_date = models.DateTimeField()

    def __str__(self):
        return f"{self.id_location} {self.concert_date}"


class Contract(MyModel):
    class Meta:
        db_table: 'contracts'
        unique_together = (("id_artist", "id_concert"),)

    id_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    id_concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.id_artist} {self.id_concert} {self.salary}"
