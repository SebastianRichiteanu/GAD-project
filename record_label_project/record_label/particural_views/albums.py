from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from record_label.models import Album
from record_label.forms import AlbumForm


def create_album(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/albums")
    context = {'form': form}
    return render(request, "album/create_album.html", context)


def list_albums(request):
    context = {"albums": Album.objects.all()}
    return render(request, "album/list_albums.html", context)


def view_album(request, id):
    context = {"album": Album.objects.get(id=id)}
    return render(request, "album/view_album.html", context)


def update_album(request, id):
    obj = get_object_or_404(Album, id=id)
    form = AlbumForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("albums/"+id)
    context = {"form": form}
    return render(request, "album/update_album.html", context)


def delete_album(request, id):
    obj = get_object_or_404(Album, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/albums")
    context = {}
    return render(request, "album/delete_album.html", context)
