from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomLoginModel
from django.contrib.auth import get_user_model
from .models import BookingModel


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "placeholder": "Username"
        })
        self.fields['password'].widget.attrs.update({
            "id": "password-field",
            "type": "password",
            "class": "form-control",
            "placeholder": "Password"
        })
    class Meta:
        model = CustomLoginModel
        fields = '__all__'

User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'input id': 'username',
            'type': 'text',
            'name': 'username',
            'placeholder': 'Username',
            'class': "form-control bg-white border-left-0 border-md"
        })
        self.fields['first_name'].widget.attrs.update({
            'input id': 'firstName',
            'type': 'text',
            'name': 'firstname',
            'placeholder': 'First Name',
            'class': "form-control bg-white border-left-0 border-md"
        })
        self.fields['last_name'].widget.attrs.update({
            'input id': 'lastName',
            'type': 'text',
            'name': 'lastname',
            'placeholder': 'Last Name',
            'class': "form-control bg-white border-left-0 border-md"
        })
        self.fields['email'].widget.attrs.update({
            'input id': 'email',
            'type': 'email',
            'name': 'email',
            'placeholder': 'Email Address',
            'class': "form-control bg-white border-left-0 border-md"
        })
        self.fields['password1'].widget.attrs.update({
            'input id': 'password',
            'type': 'password',
            'name': 'password',
            'placeholder': 'Password',
            'class': "form-control bg-white border-left-0 border-md"
        })
        self.fields['password2'].widget.attrs.update({
            'input id': 'passwordConfirmation',
            'type': 'password',
            'name': 'passwordConfirmation',
            'placeholder': 'Confirm Password',
            'class': "form-control bg-white border-left-0 border-md"
        })
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomBookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Enter your name',
            'class': "form-control"
        })
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'placeholder': 'Enter your email',
            'class': "form-control"
        })
        self.fields['phone'].widget.attrs.update({
            
            'type': 'tel',
        
            'placeholder': 'Enter your phone number',
            'class': "form-control"
        })
        self.fields['visit_date'].widget.attrs.update({
            
            'type': 'date',
            
            'class': "form-control"
        })
        self.fields['num_of_pass'].widget.attrs.update({
            'type': 'number',
            'name': 'num_of_pass',
            'class': "form-control"
        })
        self.fields['query'].widget.attrs.update({
            'input id': 'textAreaExample1',
            'type': 'date',
            'name': 'number',
            'class': "form-control"
        })
    class Meta:
        model = BookingModel
        fields = '__all__'