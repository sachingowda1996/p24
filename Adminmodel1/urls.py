"""Adminmodel1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_topic/',views.create_topic,name="create_topic"),
    path('create_webpage/',views.create_webpage,name="create_webpage"),
    path('display_topic/',views.display_topics,name="display_topics"),
    path('display_topic/<id>/',views.display_topic,name="display_topic"),
    path('display_webpage/',views.display_webpages,name="display_webpages"),
    path('display_webpage/<webid>/',views.display_webpage,name="display_webpage"),
    path('search_webpage/',views.search_webpage,name="search_webpage"),

]
