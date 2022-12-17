# ⌘⥏¤⊰⫷⋑_》╣≜ 〔 [newsletter] 〕≜╠《_⋐⫸⊱¤⥑⌘

# Startproject:

## Crear:

    django-admin startapp newsletter

## core:

### core/settings.py:

*INSTALLED_APPS*

    'newsletter',

## newsletter:    

### newsletter/models.py:

    from django.db import models

    class NewsletterUser(models.Model):
        email = models.EmailField(null=False,unique=True)
        date_added = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
            return self.email

    class newsletter(models.Model):
        name    = models.CharField(max_length=250)
        subject = models.CharField(max_length=250)
        body    = models.TextField(blank=True,null=True)
        email   = models.ManyToManyField(NewsletterUser)
        created = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
            return self.name



    
## Migraciones:

    python manage.py makemigrations

    python manage.py migrate

## newsletter/forms.py:

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

## newsletter/views.py:


# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗