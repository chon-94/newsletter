# ⌘⥏¤⊰⫷⋑_》╣≜ 〔 [Ambiente] 〕≜╠《_⋐⫸⊱¤⥑⌘

# Startproject:

## Crear:

    python manage.py startapp dashboard

# core:

### core/settings.py:

*INSTALLED_APPS*

    'dashboard',

# dashboard: 

## dashboard/urls.py:

    from django.urls import path
    from .views import DashboarHomeView

    app_name="dashboard"
    urlpatterns = [
        path('',DashboarHomeView.as_view(),name="home"),
    ]

## dashboard/views.py:

    from django.shortcuts import render

    from django.views.generic import TemplateView
    # Create your views here.
    class DashboarHomeView(TemplateView):  
        template_name="dashboard/index.html"    

# core:

## core/urls.py:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    
    
    ]

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗