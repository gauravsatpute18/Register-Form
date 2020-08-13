from django import forms
from .models import User

class Registrationform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname','lastname','address','phone','email','password']
        widgets = {
            'firstname' : forms.TextInput(attrs={'class':'form-control'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }