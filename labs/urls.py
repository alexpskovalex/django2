"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import datetime
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from .forms import BootstrapAuthForm
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path("", views.about, name="about"),
    path("onas/", views.onas, name="onas"),
    path("contact/", views.contact, name="contact"),
    path("links/", views.links, name="links"),
    path("services/", views.services, name="services"),
    path("pool/", views.pool, name="pool"),
    path("video/", views.video, name="video"),
    path("new_blog/", views.new_blog, name="new_blog"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html",
            extra_context={"title": "Вход", "year": datetime.now().year},
            authentication_form=BootstrapAuthForm,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path("registration/", views.registration, name="registration"),
    path("blog/", views.blog, name="blog"),
    path("blogpost/<int:parametr>/", views.blogpost, name="blogpost"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
