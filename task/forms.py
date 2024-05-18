from django import forms
from .models import Task
from datetime import datetime

class TaskForm(forms.ModelForm):
    due_date_date = forms.DateField(widget=forms.DateInput())
    due_date_time = forms.TimeField(widget=forms.TimeInput())
    
    class Meta:
        model = Task
        fields = ['name', 'description', 'completed', 'assigned_to']

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('due_date_date')
        time = cleaned_data.get('due_date_time')

        if not date:
            raise forms.ValidationError("The date field is required")
        
        if not time:
            raise forms.ValidationError("The time field is required")
        
        # Combine date and time into a single datetime object
        cleaned_data['due_date'] = datetime.combine(date, time)
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # manually set the due_date field
        instance.due_date = self.cleaned_data.get('due_date')

        if commit:
            instance.save()
        return instance