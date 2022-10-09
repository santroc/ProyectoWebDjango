from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from .models import Post
from UserManagement.models import  Avatar
from django.contrib import messages
from django.shortcuts import redirect

#Login, Logout y sign-up
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
#from ProyectoBlog.forms import UserEditForm, ChangePasswordForm, AvatarFormulario
from django.contrib.auth.models import User

#Decorador para requerir inicio de sesión
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None

    return render(request, 'padreBlog.html', {'avatar': avatar})

@login_required
def addPost(request):

    if (request.method == 'POST' and request.FILES['image']):
        post = Post(title= request.POST['title'], content= request.POST['content'], subtitle= request.POST['subtitle'], image= request.FILES['image'])
        post.save()
        messages.success(request, '¡Post agregado con éxito!')
        avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        return render(request, 'post.html', {'avatar': avatar})
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'post.html', {'avatar': avatar})

def busquedaPost(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'search_form.html', {'avatar': avatar})

def buscar(request):
    if request.GET['title']:
        avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        title = request.GET['title']
        objects = Post.objects.filter(title__icontains=title)
        object_name = 'Posts'
        #respuesta = f"Estoy buscando la camada: {request.GET['camada']}"
        return render(request, 'search_results.html', {"objects": objects, "title": title, "object_name": object_name, 'avatar': avatar})
    else:
        respuesta = 'No encontré nada  :('
    return HttpResponse(respuesta)

def deletePost(request, post_id):

    post = Post.objects.get(id = post_id)
    post.delete()

    return render(request, 'padreBlog.html')


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    model = Post
    template_name = 'padreBlog.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        avatar = Avatar.objects.filter(user = self.request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        context['avatar'] = avatar
        return context
    

class PostDetail(generic.DetailView):

    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        avatar = Avatar.objects.filter(user = self.request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        context['avatar'] = avatar
        return context

class PostDelete(generic.DeleteView):
    template = 'post_confirm_delete.html'
    model = Post
    success_url = "/pages/"

    def get_context_data(self, **kwargs):
        context = super(PostDelete, self).get_context_data(**kwargs)
        avatar = Avatar.objects.filter(user = self.request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        context['avatar'] = avatar
        return context

class PostUpdate(generic.UpdateView):
    model = Post
    #template = 'post.html'
    success_url = "/pages/"
    fields = ['title', 'content', 'subtitle']
    #Nota mental, acá puede estar el tema de poder modificar las imágenes si se es Admin o no en el sistema

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data(**kwargs)
        avatar = Avatar.objects.filter(user = self.request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        context['avatar'] = avatar
        return context

# def login_request(request):
    
#     if (request.method == 'POST'):
#         form = AuthenticationForm(request, data = request.POST)
#         if form.is_valid():
#             user = form.cleaned_data.get('username')
#             pwd = form.cleaned_data.get('password')

#             user = authenticate(username = user, password = pwd)

#             if (user is not None):
#                 login(request, user)
#                 messages.success(request, f'Bienvenido {user}')
#                 return redirect('/pages/')
#             else: #A este ELSE nunca entramos
#                 print('Error de datos ingresados')
#                 messages.success(request, '¡Error, datos erróneos!')
#                 return redirect('/pages/login')
#         else:
#             messages.error(request, '¡Error, datos erróneos!')
#             return redirect('/pages/login')
#     form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def register(request):

#     if (request.method == 'POST'):
#         form = UserRegisterForm(request.POST)
#         #form = UserCreationForm(request.POST)
#         if (form.is_valid()):
#             form.save()
#             messages.success(request, '¡Usuario creado con éxito!')
#             return redirect('/pages/login')
#         else:
#             messages.error(request, '¡Error al intentar registrar!')
#             return redirect('/pages/register')
#             #return render(request, '/pages/register', {'form':form}) IMPORTANTE PROBAR ESTA COSA SANTIAGO
#     #form = UserCreationForm()
#     form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})

# @login_required
# def editProfile(request):
#     usuario = request.user
#     user_basic_info = User.objects.get(id = usuario.id)
#     if (request.method == 'POST'):
#         form = UserEditForm(request.POST, instance = usuario)
#         if(form.is_valid()):
#             #Datos que se van a actualizar
#             user_basic_info.username = form.cleaned_data.get('username')
#             user_basic_info.email = form.cleaned_data.get('email')
#             user_basic_info.first_name = form.cleaned_data.get('first_name')
#             user_basic_info.last_name = form.cleaned_data.get('last_name')
#             user_basic_info.save()
#             avatar = Avatar.objects.filter(user = request.user.id)
#             try:
#                 avatar = avatar[0].image.url
#             except:
#                 avatar = None
#             #return redirect('/pages/', {'avatar': avatar})
#             return render(request, 'padreBlog.html', {'avatar': avatar})
#         else:
#             avatar = Avatar.objects.filter(user = request.user.id)
#             try:
#                 avatar = avatar[0].image.url
#             except:
#                 avatar = None
#             return render(request, reverse('Inicio'), {'form': form,'avatar': avatar})
#     else:
#         form = UserEditForm(initial = {'email': usuario.email, 'username': usuario.username,
#         'first_name': usuario.first_name, 'last_name': usuario.last_name})
#     return render(request, 'editProfile.html', {'form': form, 'usuario': usuario})

# @login_required
# def change_pass(request):
#     usuario = request.user
#     if (request.method == 'POST'):
#         form = ChangePasswordForm(data = request.POST, user = request.user)
#         if (form.is_valid()):
#             user = form.save()
#             update_session_auth_hash(request, user)
#             avatar = Avatar.objects.filter(user = request.user.id)
#             try:
#                 avatar = avatar[0].image.url
#             except:
#                 avatar = None
#             return render(request, 'padreBlog.html', {'avatar': avatar})
#     else:
#         form = ChangePasswordForm(user = request.user)

#     return render(request, 'changepass.html', {'form': form, 'usuario': usuario})

# @login_required
# def profile(request):
#     avatar = Avatar.objects.filter(user = request.user.id)
#     try:
#         avatar = avatar[0].image.url
#     except:
#         avatar = None
#     return render(request, 'profile.html', {'avatar': avatar})

# @login_required
# def agregarAvatar(request):

#     if(request.method == 'POST'):
#         form = AvatarFormulario(request.POST, request.FILES)
#         if(form.is_valid()):
#             user = User.objects.get(username = request.user)
#             avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
#             avatar.save()
#             avatar = Avatar.objects.filter(user = request.user.id)
#             try:
#                 avatar = avatar[0].image.url
#             except:
#                 avatar = None
#             return render(request, 'padreBlog.html', {'avatar': avatar})
#     else:
#         try:
#             avatar = Avatar.objects.filter(user = request.user.id)
#             form = AvatarFormulario()
#         except:
#             form = AvatarFormulario()
#     return render(request, 'addAvatar.html', {'form': form})