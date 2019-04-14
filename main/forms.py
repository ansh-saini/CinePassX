from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Show, MailSubscriber, Movie
import datetime

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password1', 'password2']

class BookForm(forms.Form):

	class Meta:
		fields = ['shows']

	def __init__(self, tag, *args, **kwargs):
		super(BookForm, self).__init__(*args, **kwargs)
		date = datetime.datetime.now().strftime("%Y-%m-%d")
		queryset = Show.objects.filter(date=date, movie__tag=tag)
		self.fields['shows'] = forms.ModelMultipleChoiceField(widget=forms.RadioSelect, queryset=queryset)
	
		

# class BookForm(forms.Form):
# 	date = datetime.datetime.now().strftime("%Y-%m-%d")
# 	queryset = Show.objects.filter(date=date)
# 	show = forms.ModelMultipleChoiceField(widget=forms.RadioSelect, queryset=queryset)
	
# 	class Meta:
# 		fields = ['show']

class MailSubscriberForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'control', 'id': 'mc-email'}))
	
	class Meta:
		model = MailSubscriber
		fields = ['email']

class FriendForm(forms.Form):
	username = forms.CharField(max_length=40)

	class Meta:
		fields = ['username']