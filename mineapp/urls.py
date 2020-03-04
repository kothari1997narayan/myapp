from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # new
from django.conf.urls.static import static # new
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    path('profile/',TemplateView.as_view(template_name = "profile.html")),
    path('saved/', views.SaveProfile, name = 'saved'),
 ]