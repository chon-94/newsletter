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

    from django.shortcuts import render
    
    from django.contrib import messages
    from newsletter.models import NewsletterUser

    from .forms import NewsletterUserSignUpForm
    from django.conf import settings

    from django.template.loader import render_to_string
    from django.core.mail import send_mail, EmailMessage

    def newsletter_signup(request):
        form =NewsletterUserSignUpForm(request.POST or None)

        if form.is_valid():
            instance=form.save(commit=False)
            if NewsletterUser.objects.filter(email=instance.email).exists():
                messages.warning(request, 'Email already exists.')

            else:
                instance.save()
                messages.success(request, 'Hemos enviado un correo electronico a su correo, abrelo para continuar con el entrenamiento')
                #Correo electronico
                subject="Libro de cocina"
                from_email=settings.EMAIL_HOST_USER
                to_email=[instance.email]
                            
                html_template='newsletter/email_templates/welcome.html'
                html_message=render_to_string(html_template)
                message=EmailMessage(subject,html_message, from_email, to_email)
                message.content_subtype='html'
                message.send()

        context={
            'form':form,
        }
        return render(request, 'start-here.html', context)

    def newsletter_unsubscribe(request):
        form =NewsletterUserSignUpForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            if NewsletterUser.objects.filter(email=instance.email).exists():
                NewsletterUser.objects.filter(email=instance.email).delete()
                messages.success(request, 'Email has been removed.')
            else:
                print('Email not found.')
                messages.warning(request, 'Email not found.')

        context = {
            "form": form,
        }

        return render(request, 'unsubscribe.html', context) 

## newsletter/urls.py:

    from django.urls import path
    from .views import newsletter_signup,newsletter_unsubscribe
    app_name="newsletter"
    urlpatterns = [
        path('subscribe/', newsletter_signup, name="optin"),
        path('unsubscribe/', newsletter_unsubscribe, name="unsubscribe"),
    ]

## newsletter/admin.py:

    from django.contrib import admin
    from .models import NewsletterUser,Newsletter
    # Register your models here.
    admin.site.register(NewsletterUser)
    admin.site.register(Newsletter)

## creamos nuestro usuario  

    newsletter/admin.py
    
# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗