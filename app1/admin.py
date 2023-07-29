from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.product)
admin.site.register(models.product_detail)
admin.site.register(models.user)