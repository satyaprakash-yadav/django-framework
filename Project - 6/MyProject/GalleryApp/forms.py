from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import ImageModel

class RegisterForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.label_suffix = ""  # Removes : as label suffix
        
    email = forms.EmailField(label='Email')
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'style':'width:62%'}))    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'placeholder':('Username')})
    #     self.fields['last_name'].widget.attrs.update({'placeholder':('Enter Your LastName')})
    #     self.fields['first_name'].widget.attrs.update({'placeholder':('Enter Your FirstName')})        
    #     self.fields['email'].widget.attrs.update({'placeholder':('Email')})
    #     self.fields['password1'].widget.attrs.update({'placeholder':('Enter Password')})        
    #     self.fields['password2'].widget.attrs.update({'placeholder':('Confirm password')})    

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
           'username' : forms.TextInput(attrs={'size':30,'style': 'font-size: large'}),
           'first_name' : forms.TextInput(attrs={'size':30,'style': 'font-size: large'}),
           'last_name' : forms.TextInput(attrs={'size':30,'style': 'font-size: large'})
           }

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['Title', 'Category', 'Image', 'Description']

    



