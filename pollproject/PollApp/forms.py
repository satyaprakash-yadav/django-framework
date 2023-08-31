from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import PollRecord
from django.forms import PasswordInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}), 
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name','class':'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email','class':'form-control'}),
            # 'password1': forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
            super(CreateUserForm, self).__init__(*args, **kwargs)
            self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
            self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    

# - Create Record

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = PollRecord
        fields = ['question', 'option1', 'option2', 'option3', 'option4']
        widgets = {
           'question' : forms.TextInput(attrs={'class':'form-control','style': 'font-size: large'}),
           'option1' : forms.TextInput(attrs={'class':'form-control','style': 'font-size: large'}),
           'option2' : forms.TextInput(attrs={'class':'form-control','style': 'font-size: large'}),
           'option3' : forms.TextInput(attrs={'class':'form-control','style': 'font-size: large'}),
           'option4' : forms.TextInput(attrs={'class':'form-control','style': 'font-size: large'}),
           }

