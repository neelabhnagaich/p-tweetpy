
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import check
from tweets.views import TweetDetailView,TweetListView
from accounts.views import UserTweetsDisplay
from hashapp.views import HashTagView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TweetListView.as_view(),name="home"),
    url(r'^tags/(?P<hashtag>.*)/$',HashTagView.as_view(),name="hashtag"),


    url(r'^tweet/',include('tweets.urls',namespace='tweet')),
    url(r'^user/',include('accounts.urls',namespace='profiles')),

    url(r'^api/tweet/',include('tweets.api.urls',namespace='tweet-api')),
     url(r'^api/',include('accounts.api.urls',namespace='account-api')),

    url(r'^messages/', include('chat.urls')),

    url(r'^blog/',include("blog.urls",namespace="blog")),
    

    

   



]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))