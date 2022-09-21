from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.contrib import messages

# Create your views here.
def inicio(request):

    return render(request, 'padreBlog.html')


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