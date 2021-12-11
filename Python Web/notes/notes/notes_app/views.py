from django.shortcuts import render, redirect

# Create your views here.
from notes.notes_app.forms import ProfileForm, NoteForm
from notes.notes_app.models import Profile, Note


def home(request):
    if Profile.objects.exists():
        context = {
            'notes': Note.objects.all()
        }
        return render(request, "home-with-profile.html", context)
    return create_profile(request)


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form': form,
            }
            return render(request, 'note-create.html', context)
    else:
        context = {
            'form': NoteForm(),
        }
        return render(request, 'note-create.html', context)


def edit(request, pk):
    current_note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=current_note)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form': form,
            }
            return render(request, 'note-edit.html', context)
    else:
        form = NoteForm(instance=current_note)
        context = {
            'form': form,
        }
        return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    current_note = Note.objects.get(pk=pk)
    form = NoteForm(instance=current_note)

    if request.method == 'GET':
        for name, field in form.fields.items():
            field.widget.attrs['disabled'] = True
            # field.widget.attrs['readonly'] = True

        context = {
            'form': form,
        }
        return render(request, 'note-delete.html', context)
    else:
        current_note.delete()
        return redirect('home')


def details(request, pk):
    current_note = Note.objects.get(pk=pk)
    context = {
        'note': current_note,
    }
    return render(request, 'note-details.html', context)


def profile(request):
    profile = Profile.objects.all()[0]
    notes_count = Note.objects.count()

    context = {
        'profile': profile,
        'notes_count': notes_count,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm()
        }
        return render(request, 'home-no-profile.html', context)

    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    Profile.objects.all()[0].delete()
    Note.objects.all().delete()
    return redirect('home')
