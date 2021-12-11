from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Django Post'
    }
    # return render(request, "<h2>myapp page</h2>")
    return render(request, "base.html", context)


def index_2(response):
    return HttpResponse("<h2>azz</h2>")
