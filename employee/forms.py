from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django import forms
from .models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password', 'dob',
                  'age', 'gender', 'address', 'phone', 'avatar', 'working_at', 'job']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['confirm_password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['username', 'name', 'dob', 'gender', 'age', 'address', 'avatar', 'working_at', 'job']


class ContactUpdateForm(forms.ModelForm):
    email = forms.CharField(max_length=100)
    phone = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'phone']