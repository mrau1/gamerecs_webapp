from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Entry, Rec


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            'age',
            'genre',
            'keyword',
            'theme',
            'game_modes',
            'tags',
            'platforms'
        ]


class RecForm(forms.ModelForm):
    class Meta:
        model = Rec
        fields = [
            'games'
        ]
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
#class DisplayForm(forms.ModelForm):
    #class Meta:
        #model = DisplayModel
        #field = ['games']

