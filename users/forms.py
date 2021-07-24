from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
	first_name = forms.CharField(label='Ваше имя')
	username = forms.CharField(label='Имя пользователя')
	email = forms.EmailField(label='Электронная почта', required=True)
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
	confirm_password = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)


	class Meta:
		model = User
		fields = ('username','first_name','email', 'password', 'confirm_password')


	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError(f'Имя {username} занято')
		return username


	def clean(self):
		password = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_password']
		if password != confirm_password:
			raise forms.ValidationError('Пароли не совпадают')
		return self.cleaned_data
		

class LoginForm(forms.Form):
	username = forms.CharField(label='Имя пользователя')
	password = forms.CharField(label='Пароль',widget=forms.PasswordInput)
