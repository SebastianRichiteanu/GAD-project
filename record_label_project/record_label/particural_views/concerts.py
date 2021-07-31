from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from record_label.models import Concert
from record_label.forms import ConcertForm


def create_concert(request):
    form = ConcertForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/concerts")
    context = {'form': form}
    return render(request, "concert/create_concert.html", context)


def list_concerts(request):
    context = {"concerts": Concert.objects.all()}
    return render(request, "concert/list_concerts.html", context)


def view_concert(request, id):
    context = {"concert": Concert.objects.get(id=id)}
    return render(request, "concert/view_concert.html", context)


def update_concert(request, id):
    obj = get_object_or_404(Concert, id=id)
    form = ConcertForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/concerts")
    context = {"form": form}
    return render(request, "concert/update_concert.html", context)


def delete_concert(request, id):
    obj = get_object_or_404(Concert, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/concerts")
    context = {}
    return render(request, "concert/delete_concert.html", context)
