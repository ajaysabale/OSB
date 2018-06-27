"""Credenz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from OSB import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^booking$', views.log_in),
    url(r'^choose/$', views.choose),
    url(r'^log_out/$', views.log_out),
    url(r'(?P<etname>[a-z|A-Z]+)/$', views.book),
    url(r'(?P<etname>[a-z|A-Z]+)/(?P<dayn>[a-z|A-Z]+)/(?P<slotn>[0-9]+)/$', views.final),
]
