from django.views import View
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.api import error
from django.contrib import messages
from django.contrib.auth.models import Permission, User, Group
from django.contrib import admin
import smtplib
# from decouple import config
from django.contrib.auth.forms import UserCreationForm  

#from django.core.checks import messages
#from .models import User,Perfil

#Login de Usuarios
def loginInit(request):
    #si es un metodo de envio, lo verifica
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]   
        UsuarioLog = authenticate(request, username=username, password=password)
        #Si las credenciales coinciden el usuario pasa a la pagina de registro 
        if(UsuarioLog is not None):
            login(request, UsuarioLog)
            #logica para redirigir usuarios a distintas plantillas
            return redirect(to = "/panelAdmin/")
                    
        messages.error(request, "revise sus credenciales e intente nuevamente")
        #Caso contrario manda ala pagina de login con un error
        return render(request=request, template_name="login.html", context={"error":"Falló la autenticación"})

#funcion cerrar cesion
def logOut(request):
    logout(request)
    return redirect(to ="/login")

def createUser(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect(to ="/createUser")

    else:
        f = UserCreationForm()

    return render(request, 'panelAdmin.html', {'form': f})



# Create your views here.
def templateLogin(request):
    return render(request,"login.html")

# Create your views here.
def templatePanelAdmin(request):
    
    users = User.objects.all()
    #verifica el permiso para usar la vista
    return render(request,"panelAdmin.html", {'users': users})

# aquitengoueseguir, terminaresto

def correoRecuperarContraseña(request):
    message = 'Correo'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # server.login('daviwaw566@rubeshi.com', config(MAIL_PASSWORD))
    server.login('daviwaw566@rubeshi.com')
    server.sendmail('daviwaw566@rubeshi.com', 'lulmimalma@gufum.com', message)

    server.quit()

    print("correo enviado exitosamente")
    return redirect(to ="/recuperarContraseña")
