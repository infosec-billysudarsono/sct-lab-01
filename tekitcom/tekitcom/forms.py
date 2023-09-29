from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '', 
            'id': 'username'
        }))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'password',
        }))
    
    login_type = forms.CharField(widget=forms.HiddenInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'login_type'
        }), 
        initial="PASSWORD",
        error_messages={'required': 'Please let us know what to call you!'}
        )