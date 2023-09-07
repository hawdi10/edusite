"""
URL configuration for siteback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1 import views


urlpatterns = [
    # path('login/', views.login_view, name='login'),
    # path('signup/', views.signup_view, name='signup'),
    # path('logout/', views.logout_view, name='logout'),
    # path('auth/google/', views.google_auth_view, name='google_auth'),
    path('index/', views.index , name='index'),
    path('admin/', admin.site.urls),
    path('panel_admin/', views.admin_panel),
    path('panel_admin_code/', views.admin_panel_code, name='panel_admin_code'),
    path('panel_admin_video/', views.admin_panel_video, name='panel_admin_video'),
    path('panel_admin_add_code/', views.admin_panel_code, name='panel_admin_add_code'),
    path('panel_admin_add_video/', views.admin_panel_add_video, name='panel_admin_add_video'),
    path('test/', views.test),
    path('login/', views.login, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('<slug:slug>/', views.slug_video_view, name='single_product'),

]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)