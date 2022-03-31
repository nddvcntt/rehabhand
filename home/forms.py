import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# tạo form
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Enter the password', widget=forms.PasswordInput())

    # kiểm tra pass mật khẩu nhập lại có trùng ko
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError(' Password is incorrect')

    # kiểm tra trùng username
    def clean_username(self):
        username = self.cleaned_data['username']
        # kiểm tra tất cả ký tự trong username có ký tự đặc biệt không
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError(
                'User name must contain only letters, numbers, spaces, or the underscore character')
        try:
            User.objects.get(username=username)

        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError(' Username already exists')

    # tạo account
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],
                                 email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
