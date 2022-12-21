from django.urls import path
from .views import newsletter_signup,newsletter_unsubscribe
app_name="newsletter"
urlpatterns = [
    path('subscribe/', newsletter_signup, name="optin"),
    path('unsubscribe/', newsletter_unsubscribe, name="unsubscribe"),
]