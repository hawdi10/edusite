from django.db import models

# Create your models here.
class video(models.Model):
    video_title = models.CharField(max_length=100)
    img = models.ImageField(null=True,upload_to="img/",blank=True)
    video_file = models.FileField(upload_to="videos/", validators=[FileExtensionValidator(['mp4', 'avi', 'mkv'])])
    text = models.TextField()
    video_price = models.CharField(max_length=50)
    video_price_final = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.video_title}"


class code(models.Model):
    code_title = models.CharField(max_length=100)
    code_file = models.FileField(upload_to="codes/",blank=True,null=True)
    code_price = models.CharField(max_length=50)
    code_final_price = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return f"{self.code_title}"

    class code_comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        text = models.TextField()
        created_time = models.DateTimeField(auto_now_add=True)
        updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code_title}"

    class video_comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        text = models.TextField()
        created_time = models.DateTimeField(auto_now_add=True)
        updated_time = models.DateTimeField(auto_now=True)