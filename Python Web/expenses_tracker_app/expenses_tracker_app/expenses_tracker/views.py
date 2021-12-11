from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker_app.expenses_tracker.forms import ProfileForm, ExpenseForm
from expenses_tracker_app.expenses_tracker.models import Profile, Expense


def home(request):
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        expense_costs = sum([expense.price for expense in Expense.objects.all()])
        profile.budget_left = profile.budget - expense_costs

        context = {
            'profile': profile,
            'expenses': Expense.objects.all()
        }
        return render(request, "home-with-profile.html", context)
    return create_profile(request)


def create_expenses(request):
    if request.method == 'GET':
        context = {
            'profile': Profile.objects.all()[0],
            'expense_form': ExpenseForm()
        }
        return render(request, 'expense-create.html', context)

    expense_form = ExpenseForm(request.POST)
    if expense_form.is_valid():
        expense_form.save()
        return redirect('home')

    context = {
        'profile': Profile.objects.all()[0],
        'expense_form': expense_form
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    current_expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile': Profile.objects.all()[0],
            'expense_form': ExpenseForm(instance=current_expense),
            'expense': current_expense
        }
        return render(request, 'expense-edit.html', context)
    else:
        form = ExpenseForm(request.POST, instance=current_expense)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'profile': Profile.objects.all()[0],
                'expense_form': form,
                'expense': current_expense
            }
            return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    current_expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile': Profile.objects.all()[0],
            'expense_form': ExpenseForm(instance=current_expense),
            'expense': current_expense
        }
        return render(request, 'expense-delete.html', context)
    else:
        current_expense.delete()
        return redirect('home')


def profile(request):
    profile = Profile.objects.all()[0]
    expense_costs = sum([expense.price for expense in Expense.objects.all()])
    profile.budget_left = profile.budget - expense_costs
    context = {
        'profile': profile,
        'budget_left': profile.budget_left,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm()
        }
        return render(request, 'home-no-profile.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=Profile.objects.all()[0])
        }
        return render(request, 'profile-edit.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form': form
            }
            return render(request, 'expense-edit.html', context)


def profile_delete(request):
    pass
