from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileManager(models.Manager):

    def toggle_follow(self,user,to_toggle_user):
        user_profile,created = UserProfile.objects.get_or_create(user=user)
        
        if to_toggle_user in user_profile.following.all():
            user_profile.following.remove(to_toggle_user)
            added = False
        else:
            user_profile.following.add(to_toggle_user)
            added = True
        
        return added
    
    def is_following(self,user,followed_by_user):
        user_profile,created = UserProfile.objects.get_or_create(user=user)

        if created:
            return False
        if followed_by_user in user_profile.following.all():
            return True
        
        return False
    
    def recommended(self,user,limit_to=10):
        profile = user.profile
        following = profile.following.all()
        following = profile.get_following()
        qs = self.get_queryset().exclude(user__in=following).exclude(id=profile.id).order_by("?")[:limit_to]

        return qs
  

    
    

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name ="profile")
    following = models.ManyToManyField(User,related_name='followed_by')
    objects = UserProfileManager()

    def __str__(self):
        return self.user.username
    
      
    def get_following(self):
        users   = self.following.all()
        print("*****************************")
        print(users)

        return users
        



@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    try:
        profile = instance.profile
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance)
    print("check","&&&&&&&&&&&&&&&&&")
    