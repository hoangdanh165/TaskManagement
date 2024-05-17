import datetime
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    due_date_0 = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control col-sm-8',
            'required': True,
            'type': 'date',  # specify input type as date
        })
    )
    due_date_1 = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'form-control col-sm-4',
            'required': True,
            'type': 'time',  # specify input type as time
        })
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'due_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project Name',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'required': True,
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        due_date_0 = cleaned_data.get('due_date_0')
        due_date_1 = cleaned_data.get('due_date_1')

        if due_date_0 and due_date_1:
            cleaned_data['due_date'] = datetime.datetime.combine(due_date_0, due_date_1)

        return cleaned_data