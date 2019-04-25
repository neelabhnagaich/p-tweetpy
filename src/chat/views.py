from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, ListView

from .forms import ComposeForm
from .models import Thread, ChatMessage
from accounts.models import UserProfile

User = get_user_model()

class InboxView(LoginRequiredMixin, ListView):
    template_name = 'chat/userdisplay.html'
    
    def get_queryset(self):
        userprofile =  User.objects.exclude(username=self.request.user)
       
        return userprofile
    
    
    def get_context_data(self, **kwargs):
        context = super(InboxView, self).get_context_data(**kwargs)
        print(context)
        print("context")



        # context['allUsers'] = User.objects.exclude(username=self.request.user)
        # context['recent'] = Thread.objects.all()
        # context['otheruser'] =  self.kwargs.get("username")
        # context['lastmsg'] = ChatMessage.objects.filter(thread=self.get_object()).order_by('-timestamp').last()
        


        
        return context



class ThreadView(LoginRequiredMixin, FormMixin, DetailView):
    template_name = 'chat/thread.html'
    form_class = ComposeForm
    success_url = './'


    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)


    def get_object(self):
        other_username  = self.kwargs.get("username")
        obj, created    = Thread.objects.get_or_new(self.request.user, other_username)
        if obj == None:
            raise Http404
        return obj

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        thread = self.get_object()
        user = self.request.user
        message = form.cleaned_data.get("message")
        ChatMessage.objects.create(user=user, thread=thread, message=message)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        print(context)

        context['allUsers'] = User.objects.exclude(username=self.request.user)
        context['recent'] = Thread.objects.all()
        context['otheruser'] =  self.kwargs.get("username")
        context['lastmsg'] = ChatMessage.objects.filter(thread=self.get_object()).order_by('-timestamp').last()
        


        
        return context

    
   
