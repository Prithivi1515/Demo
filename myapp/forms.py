from django import forms
from .models import User

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']