from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, Code, CustomUser
from user.forms import VideoCommentForm, CodeCommentForm,SignUpForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from social_django.utils import psa

@login_required
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@psa('social:complete')
def google_auth_view(request, backend):
    user = request.backend.do_auth(request.GET.get('access_token'))
    if user:
        login(request, user)
        return redirect('home')
    else:
        return redirect('login')

def video_detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)

    if request.method == 'POST':
        video_comment_form = VideoCommentForm(request.POST)
        if video_comment_form.is_valid():
            comment = video_comment_form.save(commit=False)
            comment.comment_video = video
            comment.user = request.user  # اختصاص کامنت به کاربر فعلی
            comment.save()
            return redirect('video_detail', video_id=video_id)
    else:
        video_comment_form = VideoCommentForm()

    return render(request, 'video_detail.html', {'video': video, 'video_comment_form': video_comment_form})

def code_detail(request, code_id):
    code = get_object_or_404(Code, pk=code_id)

    if request.method == 'POST':
        code_comment_form = CodeCommentForm(request.POST)
        if code_comment_form.is_valid():
            comment = code_comment_form.save(commit=False)
            comment.comment_code = code
            comment.user = request.user  # اختصاص کامنت به کاربر فعلی
            comment.save()
            return redirect('code_detail', code_id=code_id)
    else:
        code_comment_form = CodeCommentForm()

    return render(request, 'code_detail.html', {'code': code, 'code_comment_form': code_comment_form})
