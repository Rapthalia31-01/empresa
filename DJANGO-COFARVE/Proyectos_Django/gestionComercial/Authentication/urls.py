from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from Authentication import views


urlpatterns = [
    path('loginInit/', views.loginInit, name='loginInit'),
    path('logOut/', views.logOut, name='logOut'),
    #views templates
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.templateLogin, name='templateLoguin'),
    path('panelAdmin/', login_required(views.templatePanelAdmin), name='templatePanel'),
    path('createUser', views.createUser, name='createuser'),
    path('recuperarContraseña/', views.correoRecuperarContraseña, name='recuperarContraseña'),

]