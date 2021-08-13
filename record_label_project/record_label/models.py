from time import timezone

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
    publish_date = models.DateField(null=True)

    def __str__(self):
        return self.title

    @property
    def is_released(self):
        return self.publish_date < timezone.now().date()

    # For admin page
    def get_no_songs(self):
        return self.no_songs
    get_no_songs.short_description = "Number of songs"


class Song(MyModel):
    class Meta:
        db_table: 'songs'
    title = models.CharField(max_length=255, unique=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    publish_date = models.DateField(null=True)

    def __str__(self):
        return self.title

    @property
    def is_released(self):
        print(self.publish_date < timezone.now().date())
        return self.publish_date < timezone.now().date()


class Collaboration(MyModel):
    class Meta:
        db_table: 'collaborations'
        unique_together = (("song", "artist"),)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.song)} {str(self.artist)}"


class Location(MyModel):
    class Meta:
        db_table: 'locations'

    country = models.CharField(max_length=255, unique=False)
    city = models.CharField(max_length=255, unique=False)
    street = models.CharField(max_length=255, unique=False)
    name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return f"{self.name}: {self.country}, {self.city}"

    def get_address(self):
        return f"{self.country}, {self.city}, {self.street}"
    get_address.short_description = "Address"


class Concert(MyModel):
    class Meta:
        db_table: 'concerts'

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    concert_date = models.DateTimeField()

    def __str__(self):
        return f"{self.location} ; {self.concert_date}"


class Contract(MyModel):
    class Meta:
        db_table: 'contracts'
        unique_together = (("artist", "concert"),)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.artist} {self.concert} {self.salary}"
