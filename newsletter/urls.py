from django.urls import path
from .views import newsletter_signup

app_name="newsletter"

urlpatterns = [
    path('entrenamiento/', newsletter_signup, name="optin"),
]