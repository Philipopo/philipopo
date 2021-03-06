from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms






class SignUpForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=110, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=110,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

