from django.shortcuts import get_object_or_404, render, HttpResponseRedirect

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html', {
        'framework_name': 'Django'
    })


