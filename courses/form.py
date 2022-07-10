from django import forms
from .models import Register


class UserForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('name', 'lastname', 'email','telephone','goal','group')
