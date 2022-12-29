from django.contrib import admin
from .models import NewsletterUser,Newsletter
# Register your models here.
from .models import User

admin.site.register(User)
admin.site.register(NewsletterUser)
admin.site.register(Newsletter)