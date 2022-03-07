from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from app_login.models import User,Profile

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=('username','full_name','address_1','city','zipcode','country','phone')

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('email','password1','password2',)
