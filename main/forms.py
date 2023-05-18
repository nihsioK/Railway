from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Accept

'''''''''
class AcceptForm(ModelForm):
    pass_train = forms.BooleanField()
    class Meta:
        model = Accept
        fields = ('pass_train')
        labels = {
            'pass_train': 'Вы приняли машиниста?',
        }
        widgets = {
            'pass_train': BooleanField(attrs={'class': 'form-check-input', 'id': 'pass_train','name': 'pass_train', }),
        }'''''''''
