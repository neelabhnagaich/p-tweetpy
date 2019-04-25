from django import template
from django.contrib.auth import get_user_model

from accounts.models import UserProfile

User = get_user_model()
register = template.Library()


@register.inclusion_tag("accounts/snippets/recommend.html")
def recommended(user):
    if isinstance(user,User):
        qs = UserProfile.objects.recommended(user)
        return {"recommended":qs}