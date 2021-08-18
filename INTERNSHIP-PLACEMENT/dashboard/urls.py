from django.urls import path
from . import views
from accounts.views import aboutus
urlpatterns = [
    path('', views.studashboard),
    path('comdashboard', views.comdashboard),
    path('about', aboutus),
    path('comprofile', views.comprofile),
    path('complacement', views.complacement),
    path('cominternship', views.cominternship),
    path('comall', views.comall),
    path('stuprofile', views.stuprofile),
    path('stuplacement', views.stuplacement),
    path('stuinternship', views.stuinternship),
    path('stuall', views.stuall),
    path('createPlacement', views.createPlacement),
    path('createInternship', views.createInternship),
    path('regFormPlacement', views.regFormPlacement),
    path('regFormInternship', views.regFormInternship),
    path('search', views.search),
]
