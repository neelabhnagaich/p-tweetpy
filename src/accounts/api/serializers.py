from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields  =[
            'username',
            'first_name',
            'last_name',
            'url'
            
        ]
    
    def get_url(self,obj):
        return reverse("profiles:detail",kwargs={'username':obj.username})

    