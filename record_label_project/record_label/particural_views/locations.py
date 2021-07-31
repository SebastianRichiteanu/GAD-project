from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from record_label.models import Location
from record_label.forms import LocationForm


def create_location(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/locations")
    context = {'form': form}
    return render(request, "location/create_location.html", context)


def list_locations(request):
    context = {"locations": Location.objects.all()}
    return render(request, "location/list_locations.html", context)


def view_location(request, id):
    context = {"location": Location.objects.get(id=id)}
    return render(request, "location/view_location.html", context)


def update_location(request, id):
    obj = get_object_or_404(Location, id=id)
    form = LocationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/locations")
    context = {"form": form}
    return render(request, "location/update_location.html", context)


def delete_location(request, id):
    obj = get_object_or_404(Location, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/locations")
    context = {}
    return render(request, "location/delete_location.html", context)
