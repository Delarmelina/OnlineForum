from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    keyWords = models.CharField(max_length=255)
    whatsapp = models.BooleanField(default=False)
    content = RichTextUploadingField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class System(models.Model):
    system = models.CharField(max_length=255)

    class Program(models.Model):
        Program = models.CharField(max_length=255)
        
        class Detail(models.Model):
            Detail = models.CharField(max_length=255)