from django import forms 
from pagedown.widgets import AdminPagedownWidget
from .models import Post
from taggit.forms import *


class BlogCreationForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())
    

    class Meta:
        model = Post
        fields  = [
             'content',
             'title',
             'tags'
             
         ]
         

