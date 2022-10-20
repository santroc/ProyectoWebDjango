from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from UserManagement.models import  Avatar, PerfilUsuario
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import redirect

#Login, Logout y sign-up
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from UserManagement.forms import UserRegisterForm, UserEditForm, ChangePasswordForm, AvatarFormulario, UserProfileEditForm
from django.contrib.auth.models import User

#Decorador para requerir inicio de sesión
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_request(request):
    
    if (request.method == 'POST'):
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            print(pwd)
            if(user == 'hammy'):
                return redirect('https://www.google.com/')

            user = authenticate(username = user, password = pwd)

            if (user is not None):
                login(request, user)
                messages.success(request, f'Bienvenido {user}')
                return redirect('/pages/')
            else: #A este ELSE nunca entramos
                print('Error de datos ingresados')
                messages.success(request, '¡Error, datos erróneos!')
                return redirect('/accounts/login')
        else:
            messages.error(request, '¡Error, datos erróneos!')
            return redirect('/accounts/login')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):

    if (request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        #form = UserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request, '¡Usuario creado con éxito!')
            return redirect('/accounts/login')
        else:
            messages.error(request, '¡Error al intentar registrar!')
            return redirect('/accounts/signup')
            #return render(request, '/pages/register', {'form':form}) IMPORTANTE PROBAR ESTA COSA SANTIAGO
    #form = UserCreationForm()
    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def editProfile(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if (request.method == 'POST'):
        form = UserEditForm(request.POST, instance = usuario)
        user_profile_form =  UserProfileEditForm(request.POST, instance=request.user.perfilusuario)
        if(form.is_valid()):
            #Datos que se van a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')    
            user_basic_info.save()
            user_profile_form.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            #return redirect('/pages/', {'avatar': avatar})
            return render(request, 'padreBlog.html', {'avatar': avatar})
        else:
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
                #reverse('Inicio')
            return render(request, 'padreBlog.html', {'form': form,'avatar': avatar, 'profile_form': user_profile_form})
    else:
        form = UserEditForm(initial = {'email': usuario.email, 'username': usuario.username,
        'first_name': usuario.first_name, 'last_name': usuario.last_name})
        try:
            user_profile_form = UserProfileEditForm(initial = {'description': usuario.perfilusuario.description,'web_link': usuario.perfilusuario.web_link})
        except ObjectDoesNotExist:
            user_profile_form = UserProfileEditForm()
    return render(request, 'editProfile.html', {'form': form, 'usuario': usuario, 'profile_form': user_profile_form})

@login_required
def change_pass(request):
    usuario = request.user
    if (request.method == 'POST'):
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if (form.is_valid()):
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'padreBlog.html', {'avatar': avatar})
    else:
        form = ChangePasswordForm(user = request.user)

    return render(request, 'changepass.html', {'form': form, 'usuario': usuario})

@login_required
def profile(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'profile.html', {'avatar': avatar})

@login_required
def agregarAvatar(request):

    if(request.method == 'POST'):
        form = AvatarFormulario(request.POST, request.FILES)
        if(form.is_valid()):
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'padreBlog.html', {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario()
        except:
            form = AvatarFormulario()
    return render(request, 'addAvatar.html', {'form': form})
