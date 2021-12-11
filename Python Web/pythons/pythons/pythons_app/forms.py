from django import forms

from pythons.pythons_app.models import Python


class PythonCreateForm(forms.ModelForm):
    class Meta:
        model = Python
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'rows': '3',
                                                 'placeholder': 'Job Description'}),
            # 'work_category': forms.CharField(
            #     attrs={'class': 'form-control'}
            # ),
            'image': forms.FileInput(
                attrs={'class': 'form-control'},

            )
        }

        labels = {
            'image': 'Company Image (Not required)',
        }
