from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from webscraping import billboard_webscraping, news_webscraping


def homepage(request):
    news = news_webscraping()
    return render(request, 'homepage.html', {'news': news})


def billboard_top20(request):
    top20 = billboard_webscraping()
    return render(request, 'webscraping/billboard.html', {'top20': top20})

