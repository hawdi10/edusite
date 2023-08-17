from django import forms


class data_form(forms.Form):
    code_title = forms.CharField(
        label="Code title",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    code_file = forms.FileField(
        label="Code file",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    code_price = forms.CharField(
        label="Code price",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    code_final_price = forms.CharField(
        label="Code final price",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    code_detail = forms.CharField(
        label="Code detail",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    code_description = forms.CharField(
        label="Code description",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
