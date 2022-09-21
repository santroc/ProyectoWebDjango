from django.urls import path
from ProyectoBlog.views import *

urlpatterns = [
    path('home', PostList.as_view(), name='Inicio'),
    path(r'^(?P<pk>\d+)$', PostDetail.as_view(), name='post_detail'),
    path(r'^borrar/(?P<pk>\d+)$', PostDelete.as_view(),name="post_delete"),
    path(r'^editar/(?P<pk>)$', PostUpdate.as_view(), name = "post_update"),
    path('deletePost/<post_id>', deletePost, name='post_delete_nv'),
    path('addPost', addPost, name='addPost'),
    path('searchPost', busquedaPost, name='busquedaPost'),
    path('search/', buscar),
]