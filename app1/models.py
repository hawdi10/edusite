# models.py

from django.db import models
from django.utils.text import slugify

# # Video Model
class Video(models.Model):
    video_title = models.CharField(max_length=100)
    img = models.ImageField(null=True, upload_to="img/", blank=True)
    banner = models.ImageField(null=True, upload_to="img/", blank=True)
    video_file = models.FileField(upload_to="videos/",blank=True, null=True)
    video_description = models.TextField()
    video_price = models.CharField(max_length=50, null=True,blank=True)
    video_price_final = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='',null=False , allow_unicode=True, blank=True)


    def __str__(self):
        return f"{self.video_title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.video_title)
        super().save(*args, **kwargs)
# Code Model
class Code(models.Model):
    code_title = models.CharField(max_length=100)
    code_file = models.FileField(upload_to="codes/", blank=True, null=True)
    code_price = models.CharField(max_length=50,null=True,blank=True)
    code_final_price = models.CharField(max_length=50,null=True,blank=True)
    code_detail = models.TextField(null=True,blank=True)
    code_description = models.TextField()
    slug = models.SlugField(default='',null=False,allow_unicode=True,blank=True)

    def __str__(self):
        return f"{self.code_title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.code_title)
        super().save(*args,**kwargs)

class Top(models.Model):
    top_image = models.OneToOneField('Video',blank=False, null=False,on_delete=models.PROTECT)
    slug = models.SlugField(default='', null=False, allow_unicode=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.top_image)
        super().save(*args,**kwargs)

    def get_video_image(self):
        return self.top_image.img  # دسترسی به تصویر ویدیو

    def __str__(self):
        return f"{self.top_image}"

























