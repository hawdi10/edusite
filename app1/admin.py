from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Code)
admin.site.register(models.Video)
admin.site.register(models.CodeComment)
admin.site.register(models.VideoComment)
admin.site.register(models.CustomUser)
# admin.site.register(models.CustomUserManager)
# admin.site.register(models.PermissionsMixin)