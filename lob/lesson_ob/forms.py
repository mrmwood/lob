
from django import forms
#This allows me to use Djangos prebuilt user creation forms
from django.contrib.auth.forms import UserCreationForm
#this library is for authenticating users to make sure they are valid
from django.contrib.auth import authenticate
from lesson_ob.models import Account

#UserCreationForm - is a prebuilt user creation form available from
#Django via django.contrib.auth.forms
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

	class Meta:
		model = Account
		fields = ("email", "username", "password1", "password2")


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label="Password", widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			#cleaned_data normalises the data input into a consistent format
			#e.g. entering a date in different ways will format it into one way
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				#ValidationError - It is an area that isn't unique to any particular field in the form
				raise forms.ValidationError("Invalid login")




class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email','username')

	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
			except Account.DoesNotExist:
				return email
			raise forms.ValidationError('Email "%s" is already in use.' % email)


	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
			except Account.DoesNotExist:
				return username
			raise forms.ValidationError('Username "%s" is already in use.' % username)
