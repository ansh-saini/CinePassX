from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import datetime

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

# class BookForm(forms.Form):
# 	queryset = Show.objects.filter(time=datetime.datetime.now())
# 	show = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=docs)
	
# 	class Meta:
# 		fields = ['show']

# 	def __init__(self, request, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		show = Show.objects.filter(time=request.user)
# 		self.fields['checklist'] = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=docs)
