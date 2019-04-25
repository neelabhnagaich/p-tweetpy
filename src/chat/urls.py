
from django.conf.urls import url,include


from .views import ThreadView, InboxView

urlpatterns = [
    url(r"^$", InboxView.as_view()),
    url(r"^(?P<username>[\w.@+-]+)", ThreadView.as_view()),
    
]
