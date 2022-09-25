from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.contrib import messages
from django.shortcuts import redirect

#Login, Logout y sign-up
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from ProyectoBlog.forms import UserRegisterForm

#Decorador para requerir inicio de sesión
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):

    return render(request, 'padreBlog.html')

@login_required
def addPost(request):

    if (request.method == 'POST'):

        post = Post(title= request.POST['title'], content= request.POST['content'])
        post.save()
        messages.success(request, '¡Post agregado con éxito!')
        return render(request, 'post.html')

    return render(request, 'post.html')

def busquedaPost(request):
    return render(request, 'search_form.html')

def buscar(request):
    if request.GET['title']:

        title = request.GET['title']
        objects = Post.objects.filter(title__icontains=title)
        object_name = 'Posts'
        #respuesta = f"Estoy buscando la camada: {request.GET['camada']}"
        return render(request, 'search_results.html', {"objects": objects, "title": title, "object_name": object_name})
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

class PostDetail(generic.DetailView):

    model = Post
    template_name = 'post_detail.html'

class PostDelete(generic.DeleteView):
    template = 'post_confirm_delete.html'
    model = Post
    success_url = "/pages/home"

class PostUpdate(generic.UpdateView):
    model = Post
    #template = 'post.html'
    success_url = "/pages/home"
    fields = ['title', 'content']

def login_request(request):
    
    if (request.method == 'POST'):
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if (user is not None):
                login(request, user)
                messages.success(request, f'Bienvenido {user}')
                return redirect('/pages/home')
            else: #A este ELSE nunca entramos
                print('Error de datos ingresados')
                messages.success(request, '¡Error, datos erróneos!')
                return redirect('/pages/login')
        else:
            messages.error(request, '¡Error, datos erróneos!')
            return redirect('/pages/login')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):

    if (request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        #form = UserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request, '¡Usuario creado con éxito!')
            return redirect('/pages/login')
        else:
            messages.error(request, '¡Error al intentar registrar!')
            return redirect('/pages/register')
    #form = UserCreationForm()
    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
