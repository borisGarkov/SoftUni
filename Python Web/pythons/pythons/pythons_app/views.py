from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from pythons.pythons_app.forms import PythonCreateForm
from pythons.pythons_app.models import Python


def home(request):
    if request.method == 'GET':
        context = {
            'form': PythonCreateForm(),
        }
        return render(request, 'home.html', context)
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

        context = {
            'form': PythonCreateForm(request.POST)
        }

        return render(request, 'home.html', context)


def view_all_jobs(request):
    last_pythons = Python.objects.all()
    # Python.objects.order_by('-id')[:2]
    context = {
        'all_pythons': last_pythons
    }

    return render(request, 'all_jobs.html', context)
