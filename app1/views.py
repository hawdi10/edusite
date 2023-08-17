from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, Code
from django.views import View
from django.contrib.auth import login, logout
from . import forms

def admin_panel(request):
    return render(request, 'admin_panel.html')

def index(request):
    return render(request, 'index.html')

def admin_panel_code(request):
    codes = Code.objects.all()
    return render(request, 'admin_panel_detail.html',context={"codes": codes})

def admin_panel_video(request):
    videos = Video.objects.all()
    return render(request, 'admin_panel_video.html',context={"videos": videos})

def admin_panel_video(request):
    videos = Video.objects.all()
    return render(request, 'admin_panel_video.html',context={"videos": videos})

def admin_panel_add_code(request):
    return render(request, 'admin_panel_add_code.html')

def admin_panel_add_video(request):
    return render(request, 'admin_panel_add_video.html')

def post(self, request):
    add_code = forms.data_form(request.POST)
    if add_code.is_valid():
        code_title_data = add_code.cleaned_data.get("code_title")
        code_file_data = add_code.cleaned_data.get("code_file")
        code_price_data = add_code.cleaned_data.get("code_price")
        code_final_price_data = add_code.cleaned_data.get("code_final_price")
        code_detail_data = add_code.cleaned_data.get("code_detail")
        code_description_data = add_code.cleaned_data.get("code_description")
        final_code_data = Code(code_title=code_title_data,
                                code_file=code_file_data,
                                code_price=code_price_data,
                                code_final_price=code_final_price_data,
                                code_detail=code_detail_data,
                                code_description=code_description_data
            )
        final_code_data.save()
        return redirect("panel_admin_code")