from django.shortcuts import render, redirect

# Create your views here.
from recipes.recipes_app.forms import RecipeForm
from recipes.recipes_app.models import Recipe


def index(request):
    context = {
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form': form,
            }
            return render(request, 'create.html', context)
    else:
        context = {
            'form': RecipeForm(),
        }
        return render(request, 'create.html', context)


def edit(request, pk):
    current_recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=current_recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form': form,
            }
            return render(request, 'edit.html', context)
    else:
        form = RecipeForm(instance=current_recipe)
        context = {
            'form': form,
        }
        return render(request, 'edit.html', context)


def delete(request, pk):
    current_recipe = Recipe.objects.get(pk=pk)
    form = RecipeForm(instance=current_recipe)

    if request.method == 'GET':
        for name, field in form.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True

        context = {
            'form': form,
        }
        return render(request, 'delete.html', context)
    else:
        current_recipe.delete()
        return redirect('home')


def details(request, pk):
    current_recipe = Recipe.objects.get(pk=pk)
    current_recipe.ingredients = current_recipe.ingredients.split(', ')
    context = {
        'recipe': current_recipe,
    }
    return render(request, 'details.html', context)
