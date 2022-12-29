# ⌘⥏¤∵∴┊⊰⫷⋑_》╣≜ 〔 [Usuario] 〕≜╠《_⋐⫸⊱┊∴∵¤⥑⌘

# Usuario:
Para crear un usuario simple:

    python manage.py createsuperuser

si queremos un super usuario personalizado
instalamos el Django-allauth

luego:

## core/settings.py:

    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    ]


    SITE_ID = 1

*INSTALLED_APPS*

    'django.contrib.sites',
    'allauth','allauth.account',
    'allauth.socialaccount',

## core/urls.py:

    path('accounts/', include('allauth.urls')),

## Migrar:

    python manage.py migrate

despues de esto podemos configurar 
al usuario dentro de una aplicacion
por ejemplo en bitacora...
jajaja...

Y para eso nos vamos a los modelos


# ⌘⥏¤∵∴┊⊰⫷⋑_》╣≜ 〔 [Configurar] 〕≜╠《_⋐⫸⊱┊∴∵¤⥑⌘

# Configurar:
solo importamos esto

## bitacora/models.py:

    from django.contrib.auth.models import AbstractUser
creamos esta clase

    class User(AbstractUser):
        pass

        def __str__(self):
            return self.username


## core\settings.py:
final

    AUTH_USER_MODEL = 'blog.User'

migraciones:
deberiamos de borrar la migracion en posts y tambien la base de datos crear

nota me salia unmensajito para rellenar un valor inexisten o algo asi pero despues no xd

    python manage.py makemigrations blog
migrar

    python manage.py migrate

crear el super user:

    python manage.py createsuperuser

qwerty852as46df79

## blog\admin.py:

    from .models import User

    admin.site.register(User)

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗ 