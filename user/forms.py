

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app1.models import VideoComment, CodeComment, CustomUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
class VideoCommentForm(forms.ModelForm):
    class Meta:
        model = VideoComment
        fields = ['text']

class CodeCommentForm(forms.ModelForm):
    class Meta:
        model = CodeComment
        fields = ['text']

#فرم ثبت نام
class register_form(forms.Form):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': "نام و نام خانوادگی"})
    )
    password = forms.CharField(
        label="پسورد",
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': "پسورد"})
    )
    confirm = forms.CharField(
        label="تکرار پسورد",
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': "تکرار پسورد"})
    )