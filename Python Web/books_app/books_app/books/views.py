from django.shortcuts import render, redirect

# Create your views here.
from books_app.books.forms import BookForms
from books_app.books.models import Book


def index(request):
    context = {
        'books': Book.objects.all(),
    }

    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        form = BookForms()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)
    else:
        form = BookForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'create.html', context)


def edit(request, pk):
    current_book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForms(instance=current_book)
        context = {
            'form': form
        }
        return render(request, 'edit.html', context)
    else:
        form = BookForms(request.POST, instance=current_book)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'edit.html', context)


def delete(request, pk):
    current_book = Book.objects.get(pk=pk)
    current_book.delete()
    return redirect('index')
