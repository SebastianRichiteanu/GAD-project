from django.core.paginator import Paginator
from record_label.models import *


def list_model(request, model, search_by='name', obj_per_page=5):
    if 'q' in request.GET:
        q = request.GET.get('q')
        if search_by == 'name':
            models = model.objects.filter(name__icontains=q)
        elif search_by == 'title':
            models = model.objects.filter(title__icontains=q)
        elif search_by == 'artist':
            models = model.objects.filter(artist__name__icontains=q)
        elif search_by == 'song':
            models = model.objects.filter(song__title__icontains=q)
        elif search_by == 'location':
            models = model.objects.filter(location__name__icontains=q)
    else:
        models = model.objects.all()
    paginator = Paginator(models, obj_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return context
