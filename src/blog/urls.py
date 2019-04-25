from django.conf.urls import url
from django.contrib import admin
from blog import views
from blog.views import TagSearchView,BlogDetailView,BlogCreateView

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$',views.home,name='blog-home'),
    url(r'^search/(?P<tag>.*)/$',TagSearchView.as_view(),name='blog-search'),
    url(r'^detail/(?P<pk>\d+)/$',BlogDetailView.as_view(),name='blog-detail'),
    url(r'^create/',BlogCreateView.as_view(),name='blog-create'),




   

   
    # url(r'^register',users_views.register,name='register'),
    # url(r'login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    # url(r'logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    # url(r'^profile',users_views.profile,name='profile'),


]
