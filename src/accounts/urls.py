
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import UserTweetsDisplay,UserFollowView,UserRegistrationView,LogView

urlpatterns = [

    url(r'^log/$',LogView.as_view(),name='log'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^login_register/$',UserRegistrationView.as_view(),name='login_register'),


    url(r'^(?P<username>[\w.@+-]+)/$',UserTweetsDisplay.as_view(),name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$',UserFollowView.as_view(),name='follow'),


    ]

