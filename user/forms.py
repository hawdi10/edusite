

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
