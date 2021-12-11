from django import forms

from todo_project.todo_app.models import Todo


class UserForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(
        widget=forms.Textarea()
    )


class UserForm2(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
