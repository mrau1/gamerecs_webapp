from django.forms import ModelForm
from .models import input

class InputForm(ModelForm):
    class Meta:
        model = input
        fields = '__all__'
