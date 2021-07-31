from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from record_label.models import Song
from record_label.forms import SongForm


def create_song(request):
    form = SongForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/songs")
    context = {'form': form}
    return render(request, "song/create_song.html", context)


def list_songs(request):
    context = {"songs": Song.objects.all()}
    return render(request, "song/list_songs.html", context)


def view_song(request, id):
    context = {"song": Song.objects.get(id=id)}
    return render(request, "song/view_song.html", context)


def update_song(request, id):
    obj = get_object_or_404(Song, id=id)
    form = SongForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/songs")
    context = {"form": form}
    return render(request, "song/update_song.html", context)


def delete_song(request, id):
    obj = get_object_or_404(Song, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/songs")
    context = {}
    return render(request, "song/delete_song.html", context)
