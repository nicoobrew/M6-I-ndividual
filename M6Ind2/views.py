from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioForm
from .models import Usuario
from .forms import RegistroUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request, 'M6Ind2/landing.html')

def clientes(request):
    usuarios = Usuario.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, 'M6Ind2/usuarios.html', contexto)

def createUsuario(request):
    if request.method == "POST":
        formulario_post = UsuarioForm(request.POST)
        if formulario_post.is_valid():
            formulario_post.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('M6Ind2:register')
        else:
            messages.error(request, 'Ha ocurrido un error al crear el usuario. Por favor, verifica los datos ingresados.')

    formulario_get = UsuarioForm()
    return render(request, 'M6ind2/register.html', {'formulario': formulario_get})

# def registro(request):
#     if request.method == "POST":
#         formulario_p = RegistroUsuarioForm(request.POST)
#         if formulario_p.is_valid():
#             username = formulario_p.cleaned_data["username"]
#             messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')
#             formulario_p.save()
#             return redirect('M6Ind2:landing')
#         else:
#             messages.error(request, "Hubo un error en el registro")
#     formulario = RegistroUsuarioForm()
#     return render(request, 'M6Ind2/registro.html', {'formulario': formulario})

# @login_required
# def perfil(request):
#     return render(request, 'users/perfil.html')

def registro(request):
    if request.method == "POST":
        formulario_p = RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            usuario = formulario_p.save(commit=False)
            grupo_seleccionado = formulario_p.cleaned_data["tipo_usuario"]
            if grupo_seleccionado == 'administrador':
                grupo = Group.objects.get(name='administrador')
            elif grupo_seleccionado == 'usuario':
                grupo = Group.objects.get(name='usuario')
            usuario.save()
            usuario.groups.add(grupo)
            username = formulario_p.cleaned_data["username"]
            messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')
            return redirect('M6Ind2:landing')
        else:
            messages.error(request, 'Hubo un error en el registro')

    formulario = RegistroUsuarioForm()
    return render(request, "M6Ind2/registro.html", {'formulario':formulario})