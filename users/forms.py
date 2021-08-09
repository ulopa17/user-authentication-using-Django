from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
# from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        strip=False,
    )
    class Meta:
        model = User
        fields = ['username', 'email']

        # removing django helper fields on the sign up form
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
            'password': None,
        }

        def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            
            
            # for name, field in self.fields.items():
            #     field.widget.attrs.update({'class': 'input'})
            # self.fields['username'].widgets.attrs.update({'class':'input', 'placeholder':'Username'})
            # self.fields['email'].widgets.attrs.update({'class':'input', 'placeholder':'E-mail'})
            # self.fields['password1'].widgets.attrs.update({'class':'input', 'placeholder':'Password'})
            # self.fields['password2'].widgets.attrs.update({'class':'input', 'placeholder':'Password'})
