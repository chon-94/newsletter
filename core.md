# ⌘⥏¤⊰⫷⋑_》╣≜ 〔 [Core] 〕≜╠《_⋐⫸⊱¤⥑⌘

# Startproject:

## Crear:

### Opcion 1:

    django-admin startproject core .

## core:

### core/settings.py:

*INSTALLED_APPS*

    'core',

*importamos*
    
    import os
    import environ

*instalamos environ*

    env    = environ.Env()
    environ.Env.read_env()

*cortamos SECRET_KEY y DEBUG y creamos una archivo .env luego lo sustituimos* 
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG')

*Permitirá cualquier nombre de host que venga en un encabezado de Host*
    
    ALLOWED_HOSTS  = ['*']

### Tailwind:

*INSTALLED_APPS*
    
    'tailwind',

*TERMINAL*

    python manage.py tailwind init

*INSTALLED_APPS*
    
    'theme',
    
*TAILWIND_APP_NAME*

    TAILWIND_APP_NAME = 'theme'
    INTERNAL_IPS = ["127.0.0.1",]

*TERMINAL*

    python manage.py tailwind install

### core/settings.py:

    NPM_BIN = "/usr/bin/npm"

*TEMPLATES*

    'DIRS': [os.path.join(BASE_DIR, 'templates')],

*añadimos estos urls al final*

    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')] 
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_root') 
    MEDIA_URL  = '/media/' 
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media_static')

#### core/.env:
pegamos  



### Imagenes:
Para ello debemos de crear nustra carpeta static y media

### core/views.py:

    from django.shortcuts import render
    from django.views.generic import View

    class HomeView(View):
        def get(self,request, *args, **kwargs):
            context={
                
            }
            return render(request,'index.html', context)

### core/urls.py:

    from django.contrib import admin
    from django.urls import path

    from django.conf import settings 
    from django.conf.urls.static import static
    from .views import HomeView


    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', HomeView.as_view(), name="home"),
        
        ]

    if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

## Migraciones:

    python manage.py migrate

## Carpetas:
crear templates :
agregar base.html y index.html

 Crear  static y media

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗