# models.py

from django.db import models

# # Video Model
class Video(models.Model):
    video_title = models.CharField(max_length=100)
    img = models.ImageField(null=True, upload_to="img/", blank=True)
    video_file = models.FileField(upload_to="videos/",blank=True,null=True)
    video_description = models.TextField()
    video_price = models.CharField(max_length=50, null=True,blank=True)
    video_price_final = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.video_title}"

# Code Model
class Code(models.Model):
    code_title = models.CharField(max_length=100)
    code_file = models.FileField(upload_to="codes/", blank=True, null=True)
    code_price = models.CharField(max_length=50,null=True,blank=True)
    code_final_price = models.CharField(max_length=50,null=True,blank=True)
    code_detail = models.TextField(null=True,blank=True)
    code_description = models.TextField()

    def __str__(self):
        return f"{self.code_title}"


































