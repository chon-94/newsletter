from django import forms
from .models import Newsletter, NewsletterUser

class NewsletterUserSignUpForm(forms,ModelForm):
    class meta:
        model  = NewsletterUser
        fields = ['email']
        
class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name','subject','body','email']