from django.shortcuts import get_object_or_404, render, HttpResponseRedirect


def homepage(request):
    return render(request, 'homepage.html', {
        'framework_name': 'Django'
    })


