from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     date_posted = models.DateTimeField(default = timezone.now,blank=True)
     author = models.ForeignKey(User,on_delete=models.CASCADE)
     tags = TaggableManager()

     class Meta:
          ordering = ['-date_posted']



     def get_absolute_url(self):
        return reverse("blog:blog-detail",kwargs={"pk":self.pk})
     
     
    