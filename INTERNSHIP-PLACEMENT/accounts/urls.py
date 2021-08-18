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
    path("password_reset", views.password_reset_request, name="password_reset"),
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
]
