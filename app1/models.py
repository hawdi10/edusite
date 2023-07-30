# models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='customuser_set',  # Add related_name to avoid clashes
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='customuser_set',  # Add related_name to avoid clashes
        related_query_name='user',
    )

    def __str__(self):
        return self.username

# Video Model
class Video(models.Model):
    video_title = models.CharField(max_length=100)
    img = models.ImageField(null=True, upload_to="img/", blank=True)
    video_file = models.FileField(upload_to="videos/")
    text = models.TextField()
    video_price = models.CharField(max_length=50)
    video_price_final = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.video_title}"

class VideoComment(models.Model):
    comment_video = models.OneToOneField(Video, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    # ForeignKey به مدل کاربر اختصاصی
    user_video = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='video_comments_user')

# Code Model
class Code(models.Model):
    code_title = models.CharField(max_length=100)
    code_file = models.FileField(upload_to="codes/", blank=True, null=True)
    code_price = models.CharField(max_length=50)
    code_final_price = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return f"{self.code_title}"

class CodeComment(models.Model):
    comment_code = models.OneToOneField(Code, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    # ForeignKey به مدل کاربر اختصاصی
    user_code = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='code_comments_user')
