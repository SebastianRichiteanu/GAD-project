from django.core.paginator import Paginator
from record_label.models import *


def list_model(request, model, obj_per_page=1):
    if 'q' in request.GET:
        q = request.GET.get('q')
        models = model.objects.filter(name__icontains=q)
    else:
        models = model.objects.all()
    paginator = Paginator(models, obj_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return context
