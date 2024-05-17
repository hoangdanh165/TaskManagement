from django import forms
from .models import Project

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

    # Set value for due_date_0 and due_date_1 fields if the instance is passed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['due_date_0'].initial = self.instance.due_date.date()
            self.fields['due_date_1'].initial = self.instance.due_date.time()
            
    def clean_due_date(self):
        print('clean_due_date()', 30*'---')
        
        due_date_0 = self.data.get('due_date_0')
        due_date_1 = self.data.get('due_date_1')

        if not due_date_0:
            raise forms.ValidationError("The date field is required")
        
        if not due_date_1:
            raise forms.ValidationError("The time field is required")
        
        due_date_value = ' '.join([due_date_0, due_date_1])
        print(due_date_value, type(due_date_value))
        
        return due_date_value
    
    # def clean(self):
    #     print('clean()', 30*'--')
        
    #     cleaned_data = super().clean()
    #     print(cleaned_data)
    #     print(30*'--')
    #     print(self.data)
    #     print(30*'--')
        
    #     due_date_0 = cleaned_data.get('due_date_0')
    #     due_date_1 = cleaned_data.get('due_date_1')
        
    #     print('due_date_0:', due_date_0)
    #     print('due_date_1:', due_date_1)

    #     if due_date_1 is None:
    #         raise forms.ValidationError("The date field is required")
        
    #     if due_date_0 is None:
    #         raise forms.ValidationError("The time field is required")
        
    #     cleaned_data['due_date'] = datetime.datetime.combine(due_date_0, due_date_1)
        
    #     print(cleaned_data['due_date'], type(cleaned_data['due_date']))
        
    #     return cleaned_data