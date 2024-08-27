from django import forms
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation


#Registrasion Form for User register

class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))

    class Meta:
        model  = get_user_model()
        fields = ['email','username','password1','password2']


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Enter Your Profile Picher'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Address'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Bio'}))
    role = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Role'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','username','email','address','phone','bio','role','profile_pic']


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Old Password'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Repeta Password'}))