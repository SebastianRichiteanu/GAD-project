from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from record_label.models import Artist
from record_label.forms import ArtistForm


def create_artist(request):
    form = ArtistForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/artists")
    context = {'form': form}
    return render(request, "artist/create_artist.html", context)


def list_artists(request):
    context = {"artists": Artist.objects.all()}
    return render(request, "artist/list_artists.html", context)


def view_artist(request, id):
    context = {"artist": Artist.objects.get(id=id)}
    return render(request, "artist/view_artist.html", context)


def update_artist(request, id):
    obj = get_object_or_404(Artist, id=id)
    form = ArtistForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/artists")
    context = {"form": form}
    return render(request, "artist/update_artist.html", context)


def delete_artist(request, id):
    obj = get_object_or_404(Artist, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/artists")
    context = {}
    return render(request, "artist/delete_artist.html", context)
