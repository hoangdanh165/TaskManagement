from django import forms
from .models import Project
from django.core.exceptions import ValidationError
import datetime

class ProjectForm(forms.ModelForm):
    due_date_0 = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control col-sm-8',
            'required': True,
            'type': 'date',
        })
    )
    due_date_1 = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'form-control col-sm-4',
            'required': True,
            'type': 'time',
        })
    )
    
    due_date = forms.DateTimeField(required=False, widget=forms.HiddenInput())

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
        print('clean()', 30*'---')
        
        cleaned_data = super().clean()
        due_date_0 = cleaned_data.get('due_date_0')
        due_date_1 = cleaned_data.get('due_date_1')

        if due_date_1 is None:
            raise forms.ValidationError("The date field is required")
        
        if due_date_0 is None:
            raise forms.ValidationError("The time field is required")
        
        cleaned_data['due_date'] = datetime.datetime.combine(due_date_0, due_date_1)
        print(cleaned_data['due_date'], type(cleaned_data['due_date']))
        
        return cleaned_data