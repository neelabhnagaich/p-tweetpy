from .serializers import TweetModelSerializer

from rest_framework import generics

from tweets.models import Tweet

from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from .paginations import StandardResultsPagination
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

class LikeToggleAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    

    def get(self,request,pk,format=None):
        tweet_qs = Tweet.objects.filter(pk = pk)
        if request.user.is_authenticated():
            is_liked = Tweet.objects.tweet_toggle(request.user,tweet_qs.first())
            count_likes = Tweet.objects.get_likes(request.user,tweet_qs.first())
            return Response({'liked':is_liked,"count_likes":count_likes})
        return Response({'message':"invalid operation"})




class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class  = TweetModelSerializer
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)
        return Response({'message':"done"})


@method_decorator(csrf_exempt,name = 'dispatch')
class CommentAPIView(APIView):

    
    def post(self, request, *args,**kwargs):
        print(request.data,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    


class TweetListAPIView(generics.ListAPIView):

    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self,*args,**kwargs):
        context = super(TweetListAPIView,self).get_serializer_context(*args,**kwargs)
        context['request'] = self.request 
        return context

    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        if self.kwargs.get('username'):
            requested_user = self.kwargs.get('username')
            qs = qs.filter(user__username=requested_user,reply=False).order_by("-timestamp")

        else:

            qs = Tweet.objects.all()
            im_following = self.request.user.profile.get_following()

            qs1 = qs.filter(user__in=im_following,reply=False)
            qs2 = Tweet.objects.filter(user=self.request.user,reply=False)
            qs = (qs1|qs2).distinct().order_by("-timestamp")
        query = self.request.GET.get("q",None)
            
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )

        return qs


    
    