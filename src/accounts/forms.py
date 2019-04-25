from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegistrationForm(forms.Form):

    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)



    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password!=password2:
            raise forms.ValidationError("password do not match")
        return password2
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        obj = User.objects.filter(username__icontains=username)
        if obj:
            raise forms.ValidationError("username already exist")
        return username



