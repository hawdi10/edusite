from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, Code

from django.contrib.auth import login, logout


def admin_panel(request):
    return render(request, 'admin_panel.html')

def index(request):
    return render(request, 'index.html')