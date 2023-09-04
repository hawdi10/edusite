from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, Code, Top
from django.views import View
from django.contrib.auth import login, logout
from app1 import forms
from django.utils.text import slugify
from django.views import View
from siteback import urls

def admin_panel(request):
    return render(request, 'admin_panel.html')

def index(request):
    video = Video.objects.all()
    top = Top.objects.all()
    return render(request, 'index.html', context={"video": video, "top":top })

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

# def create_code(request):
#     if request.method == 'POST':
#         form = CodeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('')
#     else:
#         form = CodeForm()
#     return render(request, 'admin_panel_add_code.html', {'form': form})

def adminslug(request,slug):
    admin_slug = Code.objects.filter(id=slug)
    return render(request,'admin_panel_detail.html',context=admin_slug)


def test(request):
    return render(request,'admin_panel_detail.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')