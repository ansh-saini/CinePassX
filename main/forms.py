from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Show
import datetime

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password1', 'password2']

class BookForm(forms.Form):
	date = datetime.datetime.now().strftime("%Y-%m-%d")
	queryset = Show.objects.filter(date=date)
	show = forms.ModelMultipleChoiceField(widget=forms.RadioSelect, queryset=queryset)
	
	class Meta:
		fields = ['show']
