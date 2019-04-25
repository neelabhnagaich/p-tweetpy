
from django.conf.urls import url

from .views import TweetListAPIView,TweetCreateAPIView,LikeToggleAPIView,CommentAPIView



urlpatterns = [

    url(r'^$',TweetListAPIView.as_view(),name='list'),
    url(r'^create/$',TweetCreateAPIView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/likes/$',LikeToggleAPIView.as_view(),name='like-toggle'),
    url(r'^(?P<pk>\d+)/comment/$',CommentAPIView.as_view(),name='comment'),



    




]

