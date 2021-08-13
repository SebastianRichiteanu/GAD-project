from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from record_label.models import Contract
from record_label.forms import ContractForm
from .list import list_model


def create_contract(request):
    form = ContractForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/contracts")
    context = {'form': form}
    return render(request, "contract/create_contract.html", context)


def list_contracts(request):
    context = list_model(request, Contract)
    return render(request, "contract/list_contracts.html", context)


def view_contract(request, id):
    context = {"contract": Contract.objects.get(id=id)}
    return render(request, "contract/view_contract.html", context)


def update_contract(request, id):
    obj = get_object_or_404(Contract, id=id)
    form = ContractForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/contracts")
    context = {"form": form}
    return render(request, "contract/update_contract.html", context)


def delete_contract(request, id):
    obj = get_object_or_404(Contract, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/contracts")
    context = {}
    return render(request, "contract/delete_contract.html", context)
