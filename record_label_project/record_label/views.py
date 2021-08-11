from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from webscraping import billboard_webscraping


def homepage(request):
    return render(request, 'homepage.html', {
        'framework_name': 'Django'
    })


def billboard_top20(request):
    top20 = billboard_webscraping()
    print(top20)
    return render(request, 'webscraping/billboard.html', {'top20': top20})
