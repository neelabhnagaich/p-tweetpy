from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import DetailView
from django.views.generic import View
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.views.generic.edit import FormView
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

User  = get_user_model()

class UserTweetsDisplay(DetailView):
    model = User
    queryset = User.objects.all()
    template_name = 'accounts/user_detail.html'

    def get_object(self):
        return get_object_or_404(
                User,
                username__iexact = self.kwargs.get("username")
        )
    
    def get_context_data(self,*args,**kwargs):
        context = super(UserTweetsDisplay,self).get_context_data(*args,**kwargs)

        context["is_following"] = UserProfile.objects.is_following(self.request.user,self.get_object())
        return context

     

class UserFollowView(View):

    def get(self,request,username,*args,**kwargs):
        print(request.get_full_path())
        print("************************************************")
        toggle_user = get_object_or_404(User,username__iexact=username)
        
        if request.user.is_authenticated():
            following = UserProfile.objects.toggle_follow(request.user,toggle_user)
            
            # print("999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
        
        return redirect("/",username=username)


class UserRegistrationView(FormView):
    template_name = 'accounts/user_register.html'
    form_class = UserRegistrationForm
    success_url = '/user/login_register/'
    
    def form_valid(self,form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')

        password = form.cleaned_data.get('password')

        cr_user = User.objects.create(username=username,email=email)
        cr_user.set_password(password)
        cr_user.save()
        return super(UserRegistrationView, self).form_valid(form)
   
    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data(**kwargs)
        print(context)

        context['loginForm'] = AuthenticationForm()

        
        return context

class LogView(LoginView):
    success_url = '/user/login_register/'


    def form_invalid(self, form):
        
        return redirect("/user/login_register")
    
    







