from django import forms
from .models import Tweet

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label="",
                widget=forms.Textarea(
                    attrs={'placeholder':"your message","class":"form-control","rows":"1"}
                ))
    
    class Meta:
        model = Tweet

        fields  = [
            
            'content'
        ]

    # we can apply validations at form level also

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if content=="":
            raise forms.ValidationError("cannot be abd")
        return content

