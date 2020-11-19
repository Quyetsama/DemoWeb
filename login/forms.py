from django import forms
from django.db import models


# import re
# from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth import password_validation

# class RegistrationForm(forms.Form):
#     # class Meta:
#     #     model = MyUser
#     #     fields = ['sodu']
#     username = forms.CharField(label='Tài khoản', max_length=30, widget=forms.TextInput(attrs={'class':'regisuser'}))
#     email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'regisemail'}))
#     # widget = forms.PasswordInput ẩn mật khẩu thành dấu sao
#     password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={'class':'regispass1'}))
#     password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput(attrs={'class':'regispass2'}))
#
#     def clean_password2(self):
#         if 'password1' in self.cleaned_data:
#             password1 = self.cleaned_data['password1']
#             password2 = self.cleaned_data['password2']
#             if password1 == password2 and password1:
#                 return password2
#         raise forms.ValidationError('Mật khẩu không hợp lệ')
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if not re.search(r'^\w+$', username):
#             raise forms.ValidationError('username có kí tự đặc biệt')
#         try:
#             User.objects.get(username=username)
#         except ObjectDoesNotExist:
#             return username
#         raise forms.ValidationError('Tài khoản đã tồn tại!')
#
#     def save(self):
#         User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])

# class SetPasswordForm1(forms.Form):
#     username = forms.CharField(label='Tài khoản', max_length=30)
#     new_password1 = forms.CharField(label="New password")
#     new_password2 = forms.CharField(
#         label="New password confirmation")
#     def clean_new_password2(self):
#         password1 = self.cleaned_data.get('new_password1')
#         password2 = self.cleaned_data.get('new_password2')
#         if password1 and password2:
#             if password1 != password2:
#                 raise ValidationError('password_mismatch')
#         return password2
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if not re.search(r'^\w+$', username):
#             raise forms.ValidationError('username có kí tự đặc biệt')
#     def save(self):
#         User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['new_password1'])



from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

# Lỗi ở `view.py`, bạn import và dùng default User model của django, trong khi ở settings bạn bảo django là dùng cái MyUser của bạn. Bạn sửa cái dòng
# import User trong view thành `from django.contrib.auth import get_user_model` rồi thay hết những chỗ hiện tại bạn đang dùng `User` thành `get_user_model()`
# là đc


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'emailcss', 'placeholder': 'Email'}))
    # address = forms.CharField(max_length=255)
    class Meta:
        # lấy customuser model
        model = get_user_model()

        fields = ('username', 'email')
        # fields = ('username', 'email', 'address')
        field_classes = {'username': UsernameField}
        widgets = {
            'username': forms.TextInput(attrs={'autofocus': True, 'class': 'usercss', 'placeholder': 'Username'})
        }


from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'content'}
        widgets = {
            'content' : forms.Textarea(attrs={'class':'content'}),
        }


