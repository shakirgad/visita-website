from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class login_form(forms.ModelForm):
    username=forms.CharField(label='الاسم')
    password=forms.CharField(label='كلمة المرور',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password')
        
        
class UpdatUserForm(forms.ModelForm):
    first_name=forms.CharField(label='  الاسم الاول')
    last_name=forms.CharField(label='الاسم الاخير')
    email=forms.EmailField(label='البريد الالكترونى')
    class Meta:
        model=User
        fields=('first_name','last_name','email')
        
class UserCreationForms(UserCreationForm):
    username=forms.CharField(label='اسم المستخدم')
    first_name=forms.CharField(label='السم الاول')
    last_name=forms.CharField(label='الاسم الاخير')
    email=forms.EmailField(label='البريد الاكترونى')
    password1=forms.CharField(label='الرقم السرى', min_length=8,widget=forms.PasswordInput())
    password2=forms.CharField(label='تاكيد الرقم السرى', min_length=8,widget=forms.PasswordInput())
    class Meta:
        model=User
        fields= ('username','first_name','last_name','email','password1','password2')
        