from django.shortcuts import render, redirect

# Create your views here.
from todo_project.todo_app.forms import UserForm, UserForm2
from todo_project.todo_app.models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }

    return render(request, 'index.html', context)


def show_todos(request):
    form = UserForm2(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            # todo = Todo(
            #     title=form.cleaned_data['title'],
            #     description=form.cleaned_data['description'],
            # )
            form.save()
            return redirect('main')

    else:
        form = UserForm2()

    return render(request, 'index.html', {'form': form})
