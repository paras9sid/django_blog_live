from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django_recaptcha.fields import ReCaptchaField

class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
    captcha = ReCaptchaField()

    