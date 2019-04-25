from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

from .validators import validate_content

import json
from django.core.serializers import serialize
from django.utils.timesince import timesince



class TweetManager(models.Manager):

    def tweet_toggle(self,user,tweet_obj):
        if user in tweet_obj.likes.all():
            isliked = False
            tweet_obj.likes.remove(user)

        else:
            isliked  = True
            tweet_obj.likes.add(user)
        
        return isliked
    
    def get_likes(self,user,obj):
        return obj.likes.all().count()
    
   
    def retweet(self,user,parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj
        
        obj = self.model(
            parent = og_parent,
            user = user,
            content = parent_obj.content,
        )
        obj.save()
        return obj


# Create your models here.
class Tweet(models.Model):
    parent = models.ForeignKey("self",blank=True,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content =  models.CharField(max_length=140,validators=[validate_content])
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked',blank=True)
    reply = models.BooleanField(verbose_name="Is a reply",default=False)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    objects = TweetManager()

    def get_absolute_url(self):
        return reverse("tweet:detail",kwargs={"pk":self.pk})
    def hell(self):
        obj = Tweet.objects.filter(parent=self,reply=True)

        lst = []
        for q in obj:
            d = dict()
            d['user'] = q.user.username
            d['content'] = q.content
           
            d['time'] = timesince(q.timestamp)
            lst.append(d)
        
           
         
     
        
        # j_dic = serialize('json',obj)
        # print(j_dic,"&&&&&&&&&&&&&&&&&&&&&&&&   $$$$$$$$$")
        j_dic = json.dumps(lst)
        return j_dic,len(lst)
         
    
    
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ["-timestamp"]


    