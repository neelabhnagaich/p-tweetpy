
from django.conf.urls import url


from .views import TweetDetailView,TweetListView,TweetCreateView,TweetUpdateView,TweetDeleteView,RetweetView

from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(),name="retweet"),

   
    url(r'^search/$', TweetListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(),name='detail'),
    url(r'^create/$', TweetCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$', TweetUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$', TweetDeleteView.as_view(),name='delete'),
    






]

