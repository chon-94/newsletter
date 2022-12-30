from django.shortcuts import render
# Create your views here.
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
    return render(request, 'newsletter/start-here.html', context)

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

    return render(request, 'newsletter/unsubscribe.html', context) 