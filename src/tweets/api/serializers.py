from rest_framework import serializers
from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince
from django.urls import reverse


class ReTweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only = True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    

    likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
    # tweetdetail = serializers.SerializerMethodField()
   
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()


    def get_date_display(self,obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")
    def get_timesince(self,obj):
        return timesince(obj.timestamp)
    def get_likes(self,obj):
        return obj.likes.all().count()

    def get_did_like(self,obj):
        request = self.context.get("request")
        user = request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                return True
        return False
   
    def get_comments(self,obj):
        oct,_ = obj.hell()
       
        return oct
    
    def get_comments_count(self,obj):
        _,count = obj.hell()
        return count

    class Meta:
        model = Tweet
        fields = [
            
            'id',
            'user',
            'content',
            'date_display',
            'timestamp',
            'timesince',
             'did_like',
            'likes',
            'reply',
            'comments',
            'comments_count'
            
            
           
         
        ]

class TweetModelSerializer(serializers.ModelSerializer):
    parent_id = serializers.CharField(write_only=True,required=False)
    user = UserDisplaySerializer(read_only = True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
  
    likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
    # tweetdetail = serializers.SerializerMethodField()
    parent = ReTweetModelSerializer(read_only = True)
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()



    def get_likes(self,obj):
        return obj.likes.all().count()

    def get_did_like(self,obj):
        request = self.context.get("request")
        user = request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                return True
        return False
    
    def get_date_display(self,obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")
    
    def get_timesince(self,obj):
        return timesince(obj.timestamp)
    
    
    def get_comments(self,obj):
        oct,_ = obj.hell()
       
        return oct
    
    def get_comments_count(self,obj):
        _,count = obj.hell()
        return count


    
    


    class Meta:
        model = Tweet
        fields = [
            'parent_id',
            'id',
            'user',
            'content',
            'date_display',
            'timestamp',
            'timesince',
            'did_like',
            'likes',
            'parent',
            'reply',
            'comments',
            "comments_count",
        ]
    
    