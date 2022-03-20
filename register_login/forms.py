from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegister(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)


class AccountActivationForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(AccountActivationForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': "form-control rounded w-25 mt-1 mx-3"})


class ProfileUpdating(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdating, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': "form-control rounded w-25 mt-1 mx-3"})
        self.fields['email'].widget.attrs.update({'class': "form-control rounded w-25 mt-1 mx-3"})
        self.fields['first_name'].widget.attrs.update({'class': "form-control rounded w-25 mt-1 mx-3"})
        self.fields['last_name'].widget.attrs.update({'class': "form-control rounded w-25 mt-1 mx-3"})
