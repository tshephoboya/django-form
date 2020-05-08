from django import forms
from appTwo.models import User

class proForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        