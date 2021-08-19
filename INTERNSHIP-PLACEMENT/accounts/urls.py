from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('stusignup', views.stusignup),
    path('stusignin', views.stusignin),
    path('stusignup/stusignup', views.stusignup),
    path('stusignin/stusignin', views.stusignin),
    path('comsignup', views.comsignup),
    path('comsignin', views.comsignin),
    path('comsignup/comsignup', views.comsignup),
    path('comsignin/comsignin', views.comsignin),
    path('logout', views.logout),
    path('about', views.aboutus),
]
