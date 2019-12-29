from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(min_length=4,max_length=30,error_messages={'min_length':'用户名不少于4个字符','max_length':'用户名不能多于30个字符',
        'required':'用户名不能为空'},)
    widget =forms.TextInput(attrs={'placeholder':'请输入用户名'})
    password1 = forms.CharField(min_length=8, max_length=30,
                                error_messages={
                                    'min_length': '密码不少于8个字符',
                                    'max_length': '密码不能多于30个字符',
                                    'required': '密码不能为空',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}))
    password2 = forms.CharField(min_length=8, max_length=30,
                                error_messages={
                                    'min_length': '密码不少于8个字符',
                                    'max_length': '密码不能多于30个字符',
                                    'required': '密码不能为空',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': '请确认密码'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

    error_messages = {'password_mismatch': '两次密码不一致', }