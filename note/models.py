
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from datetime import datetime, date



class Note(models.Model):
    title =  models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    image_file = models.ImageField(blank=True, null=True, upload_to="media/")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_note", kwargs={"pk": self.pk})
    