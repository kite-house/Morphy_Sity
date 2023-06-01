"""morphy_sity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from home import views as home
from oauth2 import views as oauth2
from morphydb import views as morphydb
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name = 'home'),
    path('oauth2', oauth2.oauth2, name = 'oauth2'),
    path('oauth2/check', oauth2.oauth2DiscordCheck, name = "oauth2DiscordCheck"),
    path('morphydb', morphydb.morphydb, name = 'morphydb')
]
