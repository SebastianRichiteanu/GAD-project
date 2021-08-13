from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from record_label.models import Collaboration
from record_label.forms import CollaborationForm
from .list import list_model


def create_collaboration(request):
    form = CollaborationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/collaborations")
    context = {'form': form}
    return render(request, "collaboration/create_collaboration.html", context)


def list_collaborations(request):
    context = list_model(request, Collaboration, search_by='song')
    return render(request, "collaboration/list_collaborations.html", context)


def view_collaboration(request, id):
    context = {"collaboration": Collaboration.objects.get(id=id)}
    return render(request, "collaboration/view_collaboration.html", context)


def update_collaboration(request, id):
    obj = get_object_or_404(Collaboration, id=id)
    form = CollaborationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/collaborations")
    context = {"form": form}
    return render(request, "collaboration/update_collaboration.html", context)


def delete_collaboration(request, id):
    obj = get_object_or_404(Collaboration, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/collaborations")
    context = {}
    return render(request, "collaboration/delete_collaboration.html", context)
