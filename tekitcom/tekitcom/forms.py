from django.contrib.auth.forms import AuthenticationForm, UsernameField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-loginForm'
        self.helper.form_class = 'UserLoginForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'login'

        self.helper.add_input(Submit('Login', 'Login'))

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
        error_messages={'required': 'Login type is required'}
        )