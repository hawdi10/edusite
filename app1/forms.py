# from django import forms
#
#
# class data_form(forms.Form):
#     code_title = forms.CharField(
#         label="Code title",
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'placeholder': 'code title'
#                                       })
#     )
#     code_file = forms.FileField(
#         label="Code file",
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     code_price = forms.CharField(
#         label="Code price",
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     code_final_price = forms.CharField(
#         label="Code final price",
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     code_detail = forms.CharField(
#         label="Code detail",
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     code_description = forms.CharField(
#         label="Code description",
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
from django import forms
from .models import Video, Code

from django import forms


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

class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['code_title', 'code_file', 'code_price', 'code_final_price', 'code_detail', 'code_description']